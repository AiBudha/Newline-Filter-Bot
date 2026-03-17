import logging
from struct import pack
import re
import base64
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER, MAX_B_TN
from utils import get_settings, save_group_settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance.from_db(db)

@instance.register
class Media(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)

    class Meta:
        indexes = (
            {
                'key': [('file_name', 'text'), ('caption', 'text')],
                'name': 'search_index'
            },
        )
        collection_name = COLLECTION_NAME


async def save_file(media):
    """Save file in database"""

    # TODO: Find better way to get same file_id for same media to avoid duplicates
    file_id, file_ref = unpack_new_file_id(media.file_id)
    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
    try:
        file = Media(
            file_id=file_id,
            file_ref=file_ref,
            file_name=file_name,
            file_size=media.file_size,
            file_type=media.file_type,
            mime_type=media.mime_type,
            caption=media.caption.html if media.caption else None,
        )
    except ValidationError:
        logger.exception('Error occurred while saving file in database')
        return False, 2
    else:
        try:
            await file.commit()
        except DuplicateKeyError:      
            logger.warning(
                f'{getattr(media, "file_name", "NO_FILE")} is already saved in database'
            )

            return False, 0
        else:
            logger.info(f'{getattr(media, "file_name", "NO_FILE")} is saved to database')
            return True, 1



def _get_search_regex(query: str):
    query = query.strip()
    if not query:
        return re.compile('.', flags=re.IGNORECASE)
    
    # Improved regex for faster matching and better word boundaries
    if ' ' not in query:
        raw_pattern = r'\b' + re.escape(query) + r'\b'
    else:
        # Match all words in any order, improving relevance and speed
        words = query.split()
        raw_pattern = ''.join([f'(?=.*{re.escape(word)})' for word in words])
    return re.compile(raw_pattern, flags=re.IGNORECASE)

async def get_search_results(chat_id: int | None, query: str, file_type: str | None = None, max_results: int = 10, offset: int = 0):
    """For given query return (results, next_offset) using high-performance $text search."""
    if chat_id:
        settings = await get_settings(chat_id)
        max_results = 10 if settings.get('max_btn', True) else int(MAX_B_TN)
    
    query = query.strip()
    # Relaxed $text search for better matching
    # First try AND logic with quotes (most relevant)
    search_query = ' '.join([f'"{word}"' for word in query.split()])
    
    mongo_filter = {'$text': {'$search': search_query}}
    if file_type:
        mongo_filter['file_type'] = file_type

    projection = {'score': {'$meta': 'textScore'}}
    
    files_data = await Media.collection.find(mongo_filter, projection).sort([('score', {'$meta': 'textScore'})]).skip(offset).limit(max_results).to_list(length=max_results)
    
    # If AND logic fails, try OR logic (without quotes)
    if not files_data and offset == 0:
        search_query = query
        mongo_filter = {'$text': {'$search': search_query}}
        if file_type: mongo_filter['file_type'] = file_type
        files_data = await Media.collection.find(mongo_filter, projection).sort([('score', {'$meta': 'textScore'})]).limit(max_results).to_list(length=max_results)

    # In case $text search still returns nothing (e.g. partial words), fallback to regex
    if not files_data and offset == 0:
        regex = _get_search_regex(query)
        mongo_filter = {'$or': [{'file_name': regex}, {'caption': regex}]} if USE_CAPTION_FILTER else {'file_name': regex}
        if file_type:
            mongo_filter['file_type'] = file_type
        files_data = await Media.collection.find(mongo_filter).sort([('$natural', -1)]).skip(offset).limit(max_results).to_list(length=max_results)
        total_results = await Media.collection.count_documents(mongo_filter)
    else:
        # Re-verify count for the chosen filter
        total_results = await Media.collection.count_documents(mongo_filter)

    files = []
    for doc in files_data:
        # Map _id back to file_id for the constructor if needed
        file_id = doc.pop('_id')
        doc.pop('score', None) # Remove projection fields
        files.append(Media(file_id=file_id, **doc))
    
    next_offset = offset + max_results
    if next_offset >= total_results:
        next_offset = ''
    
    return files, next_offset, total_results

async def get_available_languages(query: str):
    """Find all languages available for a given query in a single high-performance DB call."""
    search_query = ' '.join([f'"{word}"' for word in query.split()])
    mongo_filter = {'$text': {'$search': search_query}}
    
    # Fallback for languages if $text is empty
    cursor = Media.collection.find(mongo_filter, {'file_name': 1}).limit(200)
    results = await cursor.to_list(length=200)
    
    if not results:
        regex = _get_search_regex(query)
        mongo_filter = {'$or': [{'file_name': regex}, {'caption': regex}]} if USE_CAPTION_FILTER else {'file_name': regex}
        cursor = Media.collection.find(mongo_filter, {'file_name': 1}).limit(200)
        results = await cursor.to_list(length=200)
    
    found_langs = set()
    lang_tags = ['mal', 'tam', 'hin', 'eng', 'tel', 'kan', 'multi', 'dual']
    
    for doc in results:
        fname = doc.get('file_name', '').lower()
        for tag in lang_tags:
            if tag in fname:
                found_langs.add(tag)
    return list(found_langs)

async def get_bad_files(query: str, file_type: str | None = None):
    """For given query return (results, total_results)"""
    regex = _get_search_regex(query)
    mongo_filter = {'$or': [{'file_name': regex}, {'caption': regex}]} if USE_CAPTION_FILTER else {'file_name': regex}
    
    if file_type:
        mongo_filter['file_type'] = file_type

    total_results = await Media.count_documents(mongo_filter)
    files = await Media.find(mongo_filter).sort('$natural', -1).to_list(length=total_results)

    return files, total_results

async def get_file_details(query):
    filter = {'file_id': query}
    cursor = Media.find(filter)
    filedetails = await cursor.to_list(length=1)
    return filedetails


def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")


def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")


def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref

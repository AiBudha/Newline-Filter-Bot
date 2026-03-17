

import asyncio
from pyrogram import Client, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from database.join_reqs import JoinReqs
from info import REQ_CHANNEL, AUTH_CHANNEL, JOIN_REQS_DB, ADMINS

from logging import getLogger

logger = getLogger(__name__)
INVITE_LINK = None
db = JoinReqs

async def ForceSub(bot: Client, update: Message, file_id: str | bool = False, mode: str = "checksub"):

    global INVITE_LINK
    auth = ADMINS.copy()
    if update.from_user.id in auth:
        return True

    if not AUTH_CHANNEL and not REQ_CHANNEL:
        return True

    is_cb = False
    if not hasattr(update, "chat"):
        update.message.from_user = update.from_user
        update = update.message
        is_cb = True

    # Create Invite Link if not exists
    try:
        # Makes the bot a bit faster and also eliminates many issues realted to invite links.
        if INVITE_LINK is None:
            chat_id = REQ_CHANNEL if (REQ_CHANNEL and JOIN_REQS_DB) else AUTH_CHANNEL
            if not chat_id:
                return True
            invite_link = (await bot.create_chat_invite_link(
                chat_id=int(chat_id),
                creates_join_request=True if REQ_CHANNEL and JOIN_REQS_DB else False
            )).invite_link
            INVITE_LINK = invite_link
            logger.info("Created Req link")
        else:
            invite_link = INVITE_LINK

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update, file_id)
        return fix_

    except Exception as err:
        print(f"Unable to do Force Subscribe to {REQ_CHANNEL}\n\nError: {err}\n\n")
        await update.reply(
            text="Something went Wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False

    # Mian Logic
    if REQ_CHANNEL and db().isActive():
        try:
            # Check if User is Requested to Join Channel
            user = await db().get_user(update.from_user.id)
            if user and user["user_id"] == update.from_user.id:
                return True
        except Exception as e:
            logger.exception(e, exc_info=True)
            await update.reply(
                text="Something went Wrong.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return False

    try:
        if not AUTH_CHANNEL and not REQ_CHANNEL:
            raise UserNotParticipant
        
        chat_id = REQ_CHANNEL if (REQ_CHANNEL and db().isActive()) else AUTH_CHANNEL
        if not chat_id:
            return True

        # Check if User is Already Joined Channel
        user = await bot.get_chat_member(
                   chat_id=int(chat_id), 
                   user_id=update.from_user.id
               )
        if user.status == enums.ChatMemberStatus.BANNED:
            await bot.send_message(
                chat_id=update.from_user.id,
                text="Sorry Sir, You are Banned to use me.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_to_message_id=update.message_id
            )
            return False

        else:
            return True
    except UserNotParticipant:
        text="""♦️ ** --READ THIS INSTRUCTION-- ** ♦️\n\n🗣 __ഗ്രൂപ്പിൽ ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള ലിങ്കിൽ ക്ലിക്ക് ചെയ്തു **Request To Join** ക്ലിക്ക് ചെയ്യണം. ക്ലിക് ചെയ്ത ശേഷം **Try Again** ബട്ടനിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ പ്രൈവറ്റ് ആയി അയച്ചു തരുന്നതാണ്..__😍\n\n🗣 __In Order To Get The Movies Requested By You in Our Groups, You Will Have To Click Join Channel Link Below And Click On **Request To Join** First. After That, Click **Try Again** Button. I'll Send You That Movie Privately__ 🙈"""

        buttons = [
            [
                InlineKeyboardButton("🔌 Join Channel 🔌", url=invite_link)
            ],
            [
                InlineKeyboardButton("⏳ Try Again ⏳", callback_data=f"{mode}#{file_id}")
            ]
        ]
        
        if file_id is False:
            buttons.pop()

        if not is_cb:
            await update.reply(
                text=text,
                quote=True,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=enums.ParseMode.MARKDOWN,
            )
        return False

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update, file_id)
        return fix_

    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}")
        await update.reply(
            text="Something went Wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False


def set_global_invite(url: str):
    global INVITE_LINK
    INVITE_LINK = url
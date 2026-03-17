class script(object):
    START_TXT = """✨ Hey <b>{}</b>, Welcome to <b>Movie Bot</b> – Your Premium Movie Concierge 🎬🤖

▎<b>Looking for a movie?</b> ❞
   Just send me the exact movie name, and I'll fetch the best available release from the internet instantly. 
   No ads. No confusion. Just pure movie access. 🍿💫

____________________________

▎🔔 <b>Get Exclusive Early Updates</b> ❞

Join my official channel to receive:
✅ New movie releases
✅ OTT updates
✅ Daily movie drops"""

    HELP_TXT = """<b>Hello {}</b>,

Here are the available commands and instructions for using this bot."""

    ABOUT_TXT = """<b>Bot Information:</b>
• <b>Name:</b> {}
• <b>Developer:</b> <a href='https://t.me/BabyBudha'>@BabyBudha</a>
• <b>Library:</b> <a href='https://docs.pyrogram.org/'>Pyrogram</a>
• <b>Language:</b> <a href='https://www.python.org/'>Python 3</a>
• <b>Database:</b> <a href='https://www.mongodb.com/'>MongoDB</a>
• <b>Status:</b> v5.7.1 [ Stable ]"""

    SOURCE_TXT = """All files indexed by this bot are publicly available or shared by other users. This bot serves as an index for files already uploaded to Telegram to facilitate cross-searching. We operate in compliance with DMCA and EUCD regulations. If you identify any infringing content, please contact us via <b><a href='https://t.me/BabyBudha'>support</a></b> for immediate removal."""

    MANUELFILTER_TXT = """<b>Manual Filters</b>
Filters allow you to set automated replies for specific keywords.

<b>Notes:</b>
1. Bot requires administrator privileges.
2. Only group administrators can manage filters.
3. Alert buttons are limited to 64 characters.

<b>Commands:</b>
• /filter - Add a new filter.
• /filters - List active filters in this chat.
• /del - Delete a specific filter.
• /delall - Remove all filters (Owner only)."""

    BUTTON_TXT = """<b>Inline Buttons</b>
This bot supports both URL and Alert inline buttons.

<b>Notes:</b>
1. Telegram requires all messages to have content when sending buttons.
2. Supports all Telegram media types.
3. Buttons must be formatted as Markdown.

<b>Examples:</b>
• <b>URL Button:</b> <code>[Button Text](buttonurl:https://t.me/BabyBudha)</code>
• <b>Alert Button:</b> <code>[Button Text](buttonalert:Message text)</code>"""

    AUTOFILTER_TXT = """<b>Auto Filter Setup</b>

<b>File Indexing:</b>
1. Add the bot as an administrator to your channel (private or public).
2. Forward the last message from the channel to the bot with "Quotes" to index the history.

<b>Bot Activation:</b>
1. Add the bot to your group as an administrator.
2. Use /connect to link the group in private message.
3. Use /settings in private message to enable AutoFilter."""

    CONNECTION_TXT = """<b>Connections</b>
Connect the bot to your PM to manage filters without cluttering the group.

<b>Notes:</b>
1. Only administrators can establish a connection.
2. Use <code>/connect</code> in the group to begin.

<b>Commands:</b>
• /connect - Link a chat to your PM.
• /disconnect - Unlink a chat.
• /connections - List active connections."""

    EXTRAMOD_TXT = """<b>Extra Modules</b>
Additional features available for users:

<b>Commands:</b>
• /id - Retrieve user ID.
• /info - View user profile information.
• /imdb - Search film details on IMDb.
• /search - Search media across various sources."""

    ADMIN_TXT = """<b>Administrator Tools</b>
These commands are restricted to bot administrators.

<b>System:</b>
• /logs - View recent error logs.
• /stats - Database and system statistics.
• /broadcast - Send message to all users.
• /grp_broadcast - Send message to all connected groups.

<b>Management:</b>
• /delete - Remove a specific file from DB.
• /deletefiles - Bulk delete specific patterns.
• /leave - Force bot to leave a chat.
• /disable - Deactivate bot in a chat.

<b>User Controls:</b>
• /ban - Restrict user access.
• /unban - Restore user access.

<b>Force Subscribe:</b>
• /fsub - View current fsub settings.
• /set_fsub - Set primary channel.
• /set_fsub2 - Set secondary channel.

<b>Global Filters:</b>
• /gfilter - Manage global filters.
• /delallg - Clear all global filters."""

    STATUS_TXT = """<b>System Status:</b>
• <b>Total Files:</b> <code>{}</code>
• <b>Total Users:</b> <code>{}</code>
• <b>Total Chats:</b> <code>{}</code>
• <b>Storage Used:</b> <code>{}</code>
• <b>Storage Available:</b> <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
<b>Group:</b> {}(<code>{}</code>)
<b>Members:</b> <code>{}</code>
<b>Added By:</b> {}"""

    LOG_TEXT_P = """#NewUser
<b>ID:</b> <code>{}</code>
<b>Name:</b> {}"""

    ALRT_TXT = "Hello {}, this request was initialized by another user. Please initiate your own search."

    OLD_ALRT_TXT = "Hello {}, this session has expired. Please send a new request."

    CUDNT_FND = "No direct matches found for <b>{}</b>. Did you mean one of these?"

    I_CUDNT = """<b>No results found for your request: {}</b>

Please check your spelling and try again.

<b>Format Examples:</b>
• <b>Movie:</b> Uncharted or Uncharted 2022
• <b>Series:</b> Loki S01 or Loki S01E04

Avoid using special characters like <code>:(!,./)</code>."""

    I_CUD_NT = "Unable to find media matching <b>{}</b>. Please verify the title on Google or IMDb."

    MVE_NT_FND = "Content not found in the database."

    TOP_ALRT_MSG = "Searching database..."

    MELCOW_ENG = "<b>Welcome {} to the {} group.</b>"

    OWNER_INFO = """<b>How to add the bot to your group:</b>

1. Add the bot as an administrator in your group settings.
2. Grant all necessary permissions.
3. Use the /connect command in the group.
4. The bot is now ready to serve your members."""

    REQINFO = """⚠️   𝘍𝘪𝘭𝘦𝘴 𝘸𝘪𝘭𝘭 𝘣𝘦 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 𝘪𝘯 03 𝘮𝘪𝘯𝘶𝘵𝘦𝘴. 𝘐𝘧 𝘺𝘰𝘶 𝘸𝘢𝘯𝘵 𝘵ᴏ 𝘥𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘵𝘩𝘪𝘴 𝘧𝘪𝘭𝘦, 𝘬𝘪𝘯𝘥𝘭𝘺 𝘧𝘰𝘳𝘸𝘢𝘳𝘥 𝘪𝘵 𝘵ᴏ 𝘢𝘯𝘺 𝘤ʜ𝘢𝘵 (𝘴𝘢𝘷𝘦𝘥) 𝘢𝘯𝘥 𝘴𝘵𝘢𝘳𝘵 𝘵𝘩𝘦 𝘥𝘰𝘸𝘯ʟ𝘰𝘢𝘥..."""

    NORSLTS = """<b>No Results Found:</b>
• <b>ID:</b> <code>{}</code>
• <b>Name:</b> <code>{}</code>
• <b>Message:</b> {}"""

    CAPTION = """<b>File Name:</b> {file_name}

▎⚠️ <b>Files will be deleted in 03 minutes.</b> ❞
    <i>kindly forward it to any chat (saved) and start the download...</i>"""

    IMDB_TEMPLATE_TXT = """<b>Query:</b> {query}

<b>IMDb Metadata:</b>
• <b>Title:</b> <a href={url}>{title}</a>
• <b>Genres:</b> {genres}
• <b>Year:</b> <a href={url}/releaseinfo>{year}</a>
• <b>Rating:</b> <a href={url}/ratings>{rating}</a> / 10"""
    
    ALL_FILTERS = "<b>Hello {}, please choose a filter type below:</b>"
    
    GFILTER_TXT = """<b>Global Filters</b>
These are established by administrators and active across all connected groups.

<b>Commands:</b>
• /gfilter - Create a global filter.
• /gfilters - View active global filters.
• /delg - Remove a specific global filter.
• /delallg - Clear all global filters."""
    
    FILE_STORE_TXT = """<b>File Store</b>
Generate shareable links for single or multiple files.

<b>Commands:</b>
• /batch - Create link for multiple files.
• /link - Create link for a single file.
• /pbatch - Permanent link for multiple files.
• /plink - Permanent link for a single file."""

    FSUB_TXT = """<b>Force Subscribe Configuration</b>

Manage your requirement channels here. Users must join these before accessing files.

• <b>AUTH_CHANNEL:</b> <code>{}</code>
• <b>AUTH_CHANNEL2:</b> <code>{}</code>

Click the buttons below to update or disable these channels."""

    RESTART_TXT = """<b>System Reboot Completed:</b>
• <b>Date:</b> <code>{}</code>
• <b>Time:</b> <code>{}</code>
• <b>Timezone:</b> <code>Asia/Kolkata</code>
• <b>Build:</b> <code>v2.7.1 [ Stable ]</code>"""

    LOGO = r"""
  _   _             _      _               __  __           _                 
 | \ | |           | |    (_)             |  \/  |         (_)                
 |  \| | _____      | |     _ _ __   ___   | \  / | _____   _  ___  ___        
 | . ` |/ _ \ \ /\ / / |    | | '_ \ / _ \  | |\/| |/ _ \ \ / / |/ _ \/ __|     
 | |\  |  __/\ V  V /| |____| | | | |  __/  | |  | | (_) \ V /| |  __/\__ \     
 |_| \_|\___| \_/\_/ |______|_|_| |_|\___|  |_|  |_|\___/ \_/ |_|\___||___/     
                                                                                
"""

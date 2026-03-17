<p align="center">
  <img src="https://telegra.ph/file/171925d184de01b3055dc.jpg" alt="New Line Movies Logo">
</p>
<h1 align="center">
  New Line Movies Bot
</h1>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+New+Line+Movies!;Created+by+New+Line+Movies!;A+simple+and+powerful+Bot!;Indexes+Files+above+2GB;Bot+with+double+fsub!;Start+message+with+pic!;And+more+features!)
</p>

<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-skyblue?style=for-the-badge&logo=python" alt="Python" /> </a>
<a href="https://pypi.org/project/Pyrogram/"> <img src="https://img.shields.io/pypi/v/pyrogram?color=white&label=pyrogram&logo=python&logoColor=blue&style=for-the-badge" /></a>

## Features
- [x] **Double Force Subscribe** (Configurable via Bot)
- [x] **Persistent Dynamic Config** (Stored in DB)
- [x] IMDB Template Set
- [x] Indexes Files above 2GB
- [x] PreDVD and CamRip Delete Mode
- [x] Multiple File Deletion
- [x] Settings Menu
- [x] Welcome Message
- [x] Automatic File Filtering
- [x] Bot PM File Send Mode
- [x] Auto File Send
- [x] Forward Restriction & File Protect
- [x] Global & Manual Filtering
- [x] Inline Search & IMDB Integration
- [x] Stats & User Management (Ban/Unban)
- [x] Spelling Check Feature
- [x] File Store & Auto Delete

## Commands
```
• /start - Start the bot
• /fsub - View current Force Subscribe settings (Admin)
• /set_fsub - Set primary fsub channel (Admin)
• /set_fsub2 - Set secondary fsub channel (Admin)
• /settings - Open settings menu
• /connect - Connect a group to PM
• /disconnect - Disconnect from PM
• /connections - View all connected groups
• /filter - Add manual filters
• /filters - View active filters
• /del - Delete a filter
• /delall - Delete all filters
• /gfilter - Add global filters
• /delete - Delete a specific file from index
• /deletefiles - Bulk delete specific patterns
• /imdb - Fetch info from IMDb
• /search - Search from various sources
• /info - Get user info
• /id - Get Telegram IDs
• /logs - View recent errors
• /stats - View database statistics
• /broadcast - Send message to all users
• /grp_broadcast - Send message to all connected groups
• /batch - Create link for multiple posts
• /link - Create link for a single post
```

## Variables

### Required Variables
* `BOT_TOKEN`: Your Telegram Bot Token.
* `API_ID`: Your Telegram API ID.
* `API_HASH`: Your Telegram API Hash.
* `CHANNELS`: IDs of channels to index (separated by space).
* `ADMINS`: IDs of bot administrators.
* `DATABASE_URI`: MongoDB connection string.
* `DATABASE_NAME`: MongoDB database name.
* `LOG_CHANNEL`: Channel for bot activity logs.

### Force Subscribe Variables
* `AUTH_CHANNEL`: Primary channel ID for Force Subscribe.
* `AUTH_CHANNEL2`: Secondary channel ID for Force Subscribe.
* *Note: These can also be managed in-bot via commands.*

## Deployment

### Deploy To Render
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python bot.py`
- *The bot includes a built-in health check server for Render compatibility.*

<details><summary>Deploy To Heroku</summary>
<p>
<br>
Ensure you have set all required variables in your Heroku app settings.
</p>
</details>

<details><summary>Deploy To Koyeb</summary>
<br>
<b>Set up a new service on Koyeb and connect your repository.</b>
<br>
</details>

<details><summary>Deploy To Render</summary>
<br>
<b>
Use these commands:
<br>
<br>
• Build Command: <code>pip3 install -U -r requirements.txt</code>
<br>
<br>
• Start Command: <code>python3 bot.py</code>
</b>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone [YOUR_REPO_URL]
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

<hr>

## Credits
- Developed & Maintained by: **New Line Movies**
- Library: [Pyrogram](https://github.com/pyrogram/pyrogram)

## Disclaimer
Licensed under GNU AGPL 2.0.
Selling this code is strictly prohibited.
© 2026 New Line Movies. All Rights Reserved.

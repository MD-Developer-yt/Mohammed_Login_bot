🚀 Features

📦 Core Features
Save Restricted Content — Download text, media, and files from restricted channels.
Batch Mode — Bulk download messages from public or private channels with auto-detection.
User Login — Login using /login to enable downloading capabilities.

⚙️ Customization
Set custom captions (/set_caption)
Set custom thumbnails (/set_thumb)
Auto-delete or replace specific words

💎 Premium System
Built-in system for free and premium users
Admin-controlled premium access

👑 Admin Tools
Broadcast messages
Ban / Unban users
Manage premium status

🧠 Persistent Storage
MongoDB-based user data and settings

⚙️ Environment Variables

Variable	        Description
BOT_TOKEN	        Telegram Bot Token from BotFather
API_ID	          Telegram API ID
API_HASH	        Telegram API Hash
ADMINS	          Comma-separated Admin User IDs
DB_URI	          MongoDB Connection String
DB_NAME	          Database Name (default: SaveRestricted)
LOG_CHANNEL	      Channel ID for logging users and errors
ERROR_MESSAGE	    Send error messages to users
KEEP_ALIVE	      Use an uptime service like UptimeRobot

🛠 Deployment

Render
Heroku

💻 Local Setup
Installation Steps
Clone the repository
git clone https://github.com/MD-Developer-yt/Mohammed_Login_bot.git
cd SAVE-RESTRICT-BOT
Install dependencies
pip install -r requirements.txt
Run the bot
python bot.py
🐳 Docker
docker build -t save-restricted-bot .
docker run -d --env-file .env save-restricted bot

📝 Commands

Command	Action
/start	Start the bot
/help	Get help information
/login	Login to your account
/logout	Logout from your account
/cancel	Cancel batch process
/settings	Open settings menu
/myplan	Check your current plan
/premium	View premium details
⚙️ Customization
/set_caption
/see_caption
/del_caption
/set_thumb
/view_thumb
/del_thumb
/thumb_mode
/set_del_word
/rem_del_word
/set_repl_word
/rem_repl_word
/setchat
👑 Admin Commands
Click to Expand
/broadcast
/ban / /unban
/add_premium / /remove_premium
/users
/premium_users
/set_dump
/dblink

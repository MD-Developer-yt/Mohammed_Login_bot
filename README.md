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


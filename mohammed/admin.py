#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import db
from config import ADMINS, DB_URI

@Client.on_message(filters.command("ban") & filters.user(ADMINS))
async def ban(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:** `/ban user_id`")
    try:
        user_id = int(message.command[1])
        await db.ban_user(user_id)
        await message.reply_text(f"**User {user_id} Banned Successfully 🚫**")
    except:
        await message.reply_text("Error banning user.")

@Client.on_message(filters.command("unban") & filters.user(ADMINS))
async def unban(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:** `/unban user_id`")
    try:
        user_id = int(message.command[1])
        await db.unban_user(user_id)
        await message.reply_text(f"**User {user_id} Unbanned Successfully ✅**")
    except:
        await message.reply_text("Error unbanning user.")
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

@Client.on_message(filters.command("set_dump") & filters.user(ADMINS))
async def set_dump(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.reply_text("**Usage:** `/set_dump user_id chat_id`")
    try:
        user_id = int(message.command[1])
        chat_id = int(message.command[2])
        await db.set_dump_chat(user_id, chat_id)
        await message.reply_text(f"**Dump chat set for user {user_id}.**")
    except:
        await message.reply_text("Error setting dump chat.")

@Client.on_message(filters.command("dblink") & filters.user(ADMINS))
async def dblink(client: Client, message: Message):
    await message.reply_text(f"**DB URI:** `{DB_URI}`")

@Client.on_message(filters.command(["add_unsubscribe", "del_unsubscribe"]) & filters.user(ADMINS))
async def manage_force_subscribe(client: Client, message: Message):
    await message.reply_text("Force Subscribe management feature is coming soon.")

#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

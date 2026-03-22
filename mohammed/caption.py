from pyrogram import Client, filters, enums
from pyrogram.types import Message
from database.db import db

# ======================================================
# /set_caption - Set Custom Caption
# ======================================================
@Client.on_message(filters.command("set_caption") & filters.private)
async def set_caption(client: Client, message: Message):
    user_id = message.from_user.id

    # 1. Ensure User Exists
    if not await db.is_user_exist(user_id):
        await db.add_user(user_id, message.from_user.first_name)

    # 2. Validate Input
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>⚠️ Usage Error</b>\n\n"
            "Please provide the caption text after the command.\n\n"
            "<b>Correct Format:</b>\n"
            "<code>/set_caption Your Caption Here</code>\n\n"
            "<b>Supported Placeholders:</b>\n"
            "• <code>{filename}</code> : Original File Name\n"
            "• <code>{size}</code> : File Size\n\n"
            "<i>Example:</i> <code>/set_caption File: {filename} | Size: {size}</code>",
            parse_mode=enums.ParseMode.HTML
        )

    # 3. Save to Database
    caption = message.text.split(" ", 1)[1].strip()
    await db.set_caption(user_id, caption)

    await message.reply_text(
        "<b>✅ Custom Caption Saved!</b>\n\n"
        f"<b>Preview:</b>\n<code>{caption}</code>\n\n"
        "<i>This caption will be applied to your future downloads.</i>",
        parse_mode=enums.ParseMode.HTML
    )

# ======================================================
# /see_caption - View Current Caption
# ======================================================
@Client.on_message(filters.command("see_caption") & filters.private)
async def see_caption(client: Client, message: Message):
    user_id = message.from_user.id

    # 1. Ensure User Exists
    if not await db.is_user_exist(user_id):
        await db.add_user(user_id, message.from_user.first_name)

    # 2. Fetch Caption
    caption = await db.get_caption(user_id)

    if caption:
        await message.reply_text(
            "<b>📝 Your Custom Caption</b>\n\n"
            f"<code>{caption}</code>\n\n"
            "<i>To delete this, use /del_caption</i>",
            parse_mode=enums.ParseMode.HTML
        )
    else:
        await message.reply_text(
            "<b>❌ No Caption Set</b>\n\n"
            "You are currently using the default bot caption.\n"
            "<i>Use /set_caption to customize it.</i>",
            parse_mode=enums.ParseMode.HTML
        )

# ======================================================
# /del_caption - Delete Custom Caption
# ======================================================
@Client.on_message(filters.command("del_caption") & filters.private)
async def del_caption(client: Client, message: Message):
    user_id = message.from_user.id

    # 1. Ensure User Exists
    if not await db.is_user_exist(user_id):
        await db.add_user(user_id, message.from_user.first_name)

    # 2. Check if caption exists
    caption = await db.get_caption(user_id)

    if not caption:
        return await message.reply_text(
            "<b>⚠️ No Caption Found</b>\n\n"
            "You don't have a custom caption set.",
            parse_mode=enums.ParseMode.HTML
        )

    # 3. Delete from Database
    await db.del_caption(user_id)

    await message.reply_text(
        "<b>🗑 Custom Caption Removed</b>\n\n"
        "<i>Your uploads will now use the default bot caption.</i>",
        parse_mode=enums.ParseMode.HTML
    )

#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

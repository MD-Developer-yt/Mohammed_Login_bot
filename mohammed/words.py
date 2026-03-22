#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import db

@Client.on_message(filters.command("set_del_word") & filters.private)
async def set_del_word(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:** `/set_del_word word1 word2 ...`\n\nThese words will be automatically removed from captions and filenames.")

    words = message.command[1:]
    await db.set_delete_words(message.from_user.id, words)
    await message.reply_text(f"**Added {len(words)} words to delete list.**")

@Client.on_message(filters.command("rem_del_word") & filters.private)
async def rem_del_word(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:** `/rem_del_word word1 word2 ...`")

    words = message.command[1:]
    await db.remove_delete_words(message.from_user.id, words)
    await message.reply_text(f"**Removed {len(words)} words from delete list.**")
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

@Client.on_message(filters.command("set_repl_word") & filters.private)
async def set_repl_word(client: Client, message: Message):
    # Syntax: /set_repl_word target replacement
    if len(message.command) < 3:
        return await message.reply_text("**Usage:** `/set_repl_word target replacement`\n\nExample: `/set_repl_word @OldChannel @NewChannel`")

    target = message.command[1]
    replacement = message.command[2]

    await db.set_replace_words(message.from_user.id, {target: replacement})
    await message.reply_text(f"**Set replacement:** `{target}` -> `{replacement}`")

@Client.on_message(filters.command("rem_repl_word") & filters.private)
async def rem_repl_word(client: Client, message: Message):
    if len(message.command) < 2:
         return await message.reply_text("**Usage:** `/rem_repl_word target`")

    target = message.command[1]
    await db.remove_replace_words(message.from_user.id, [target])
    await message.reply_text(f"**Removed replacement for:** `{target}`")

#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29

import asyncio
from time import time
from helpers.filters import command
from config import BOT_USERNAME, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command(["ping", "repo", "anon", "alive"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    start = time()
    delta_ping = time() - start
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo="https://telegra.ph/file/89cbc8b8760b6abff430f.jpg",
        caption=f"""<b>ð á´©á´É´É¢ Êá´ÊÊ !</b>\n   `{delta_ping * 1000:.3f} á´s`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð sá´á´á´á´Êá´ ð", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "ð sá´á´Êá´á´ ð", url="https://github.com/AnonymousBoy1025/FallenMusic"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ð¥º á´á´á´ á´á´ Êá´ÊÊââ ð¥º", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )]
            ]
        ),
    )

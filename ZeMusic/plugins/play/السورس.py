import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7e8337bd2a650ae9a4279.jpg",
        caption = f"""<b>  ⌯ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 . .<b>\n<a href="https://t.me/KKC8C"> ⌯ 𝚂𝙾𝚄𝚁𝙲𝙴 BIG sam ⛧</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ لتنصيب بوت ›", url=f"https://t.me/Y_o_V"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/KKC8C"),         
                ],

            ]

        ),

    )

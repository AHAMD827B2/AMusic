"""
- 𝗕𝗬 : @programer_senzir
- 𝗖𝗛 : @IC_X_K
- Copyright (©️) 2024-5-5 SEN-ZIR
"""

from ZeMusic import app
from pyrogram import filters


@app.on_message(filters.command("ايدي", "id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
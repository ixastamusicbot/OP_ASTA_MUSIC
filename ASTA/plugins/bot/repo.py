from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ASTA import app
from config import BOT_USERNAME
from ASTA.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ɴᴏʙɪᴛᴀ ʀᴇᴘᴏs ⌾
 
● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ ɴᴏʙɪᴛᴀ ꭙ ᴍᴜsɪᴄ ♡゙゙

● ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ● **
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/+wPjAlUcObehiZDM1"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="ixasta1"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/ixasta1"),
],
[
InlineKeyboardButton("• ʀᴇᴘᴏ •", url=f"https://t.me/ixasta1"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

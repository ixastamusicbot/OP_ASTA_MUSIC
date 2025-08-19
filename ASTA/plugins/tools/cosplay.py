import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from ASTA import app
from config import BOT_USERNAME

ASTA = [
    [
        InlineKeyboardButton(text="✙ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✙", url=f"https://t.me/Laibaamusicbot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/+wPjAlUcObehiZDM1"),
    ],
]

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ ˹ 𝐀𝐬𝐭𝐚 ꭙ 𝐌ᴜ𝐬ɪᴄ ˼", reply_markup=InlineKeyboardMarkup(SACHIN),)

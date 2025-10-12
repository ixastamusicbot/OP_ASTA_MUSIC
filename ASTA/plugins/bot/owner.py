from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ASTA import app
from config import BOT_USERNAME
from ASTA.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬───────────────────⦿
│├───────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ʀɪsʜᴜ sᴀɴᴀᴛᴀɴɪ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ʀɪsʜᴜ ʀᴀᴊᴘᴜᴛ
│├───────────────────╯
├┼───────────────────⦿
├┤~ @ixasta1
├┤~ @ixasta
├┤~ @Laibaamusicbot
├┼──────────────────────────⦿
│├──────────────────────────╮
│├OWNER│ @ixasta1
│├──────────────────────────╯
└┴──────────────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⋏ 𝛅 𝛕 ⋏", url=f"ixasta1")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/oldskoolgc"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/ixasta1"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/ixasta1"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/Laibaamusicbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/9eq3l9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

from ... import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ASTA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/https://t.me/Laibaamusicbot?start=_tgr_wnBXNLAzMGM1"),
    ],
]


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "✦ <b>ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀ ʙɪɴ ᴛᴏ\n✦ ɢᴇᴛ ʙɪɴ ᴅᴇᴛᴀɪʟs !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("❄️")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("✨")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b>┬── ⋅ ⋅ ───── ᯽ ───── ⋅ ⋅ ──┬</b>
<b>            ❖ ʙɪɴ ғᴜʟʟ ᴅᴇᴛᴀɪʟs ❖</b>
<b>┴── ⋅ ⋅ ───── ᯽ ───── ⋅ ⋅ ──┴</b>

<b>๏ ʙᴀɴᴋ ➠</b> <tt>{resp.bank}</tt>
<b>๏ ʙɪɴ ➠</b> <tt>{resp.bin}</tt>
<b>๏ ᴄᴏᴜɴᴛʀʏ ➠</b> <tt>{resp.country}</tt>
<b>๏ ғʟᴀɢ ➠</b> <tt>{resp.flag}</tt>
<b>๏ ɪsᴏ ➠</b> <tt>{resp.iso}</tt>
<b>๏ ʟᴇᴠᴇʟ ➠</b> <tt>{resp.level}</tt>
<b>๏ ᴘʀᴇᴘᴀɪᴅ ➠</b> <tt>{resp.prepaid}</tt>
<b>๏ ᴛʏᴘᴇ ➠</b> <tt>{resp.type}</tt>
<b>๏ ᴠᴇɴᴅᴏʀ ➠</b> <tt>{resp.vendor}</tt>

<b>❖ ʙɪɴ ᴄʜᴇᴄᴋᴇᴅ ʙʏ ➠ ˹ 𝐀𝐬𝐭𝐚 ꭙ 𝐌ᴜ𝐬ɪᴄ ˼</b>""", reply_markup=InlineKeyboardMarkup(SACHIN),
        )
    except:
        return await aux.edit(f"""
๏ ʙɪɴ ɴᴏᴛ ʀᴇᴄᴏɢɴɪᴢᴇᴅ, ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ʙɪɴ.""")

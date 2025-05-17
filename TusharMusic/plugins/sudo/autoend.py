from pyrogram import filters
from pyrogram.types import Message

from TusharMusic import app
from TusharMusic.misc import SUDOERS
from TusharMusic.utils.database import autoend_off,autoend_on,autoleave_off, autoleave_on,is_autoend,is_autoleave


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    zerostate = await is_autoend()
    usage = f"<b>Example :</b>\n\n/autoend [Enable | Disable]\n\n Current state : {zerostate}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state in ["enable","on","yes"]:
        await autoend_on()
        await message.reply_text(
            "» Auto end stream enabled.\n\nAssistant will automatically leave the video chat after the few mins when no one is listening."
        )
    elif state in ["disable","off","no"]:
        await autoend_off()
        await message.reply_text("» Auto end stream enabled.")
    else:
        await message.reply_text(usage)

@app.on_message(filters.command("autoleave") & SUDOERS)
async def auto_leave_chat(_, message: Message):
    zerostate = await is_autoleave()
    usage = f"<b>Example :</b>\n\n/autoleave [Enable | Disable]\n\n Current state : {zerostate}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state in ["enable","on","yes"]:
        await autoleave_on()
        await message.reply_text(
            "» Auto leave chat Enabled.\n\n.Assistant will automatically leave the video chat after the few mins when no one is listening"
        )
    elif state in ["disable","off","no"]:
        await autoleave_off()
        await message.reply_text("» Auto leave chat Disabled.")
    else:
        await message.reply_text(usage)
        

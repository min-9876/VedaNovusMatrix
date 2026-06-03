import asyncio
import uvloop
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER

# Event Loop ကို အတင်းသတ်မှတ်ပေးခြင်း (Error မတက်အောင်)
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

class Tushar(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        # Client ကို initialize လုပ်ခြင်း
        super().__init__(
            name="TusharMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,  # ပိုမြန်စေရန် memory တွင်သာ သိမ်းခြင်း
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        # Bot ကို စတင်ခြင်း
        await super().start()
        
        # Bot အချက်အလက်များ ရယူခြင်း
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # Log group သို့ message ပို့ခြင်း
        try:
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"<u><b>» {self.mention} Bot started :</b></u>\n\n"
                     f"ID : <code>{self.id}</code>\n"
                     f"Name : {self.name}\n"
                     f"Username : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        # Admin ဟုတ်မဟုတ် စစ်ဆေးခြင်း
        try:
            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Please promote your bot as an admin in your log group/channel."
                )
                exit()
        except Exception:
            LOGGER(__name__).error("Cannot get chat member. Check if bot is in the log group.")
            exit()

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        # Bot ကို ရပ်တန့်ခြင်း
        await super().stop()

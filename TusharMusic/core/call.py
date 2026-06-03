import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    TelegramServerError,
)
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded

import config
from TusharMusic import LOGGER, YouTube, app
from TusharMusic.misc import db
from TusharMusic.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    get_loop,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from TusharMusic.utils.exceptions import AssistantErr
from TusharMusic.utils.formatters import check_duration, seconds_to_min, speed_converter
from TusharMusic.utils.inline.play import stream_markup
from TusharMusic.utils.stream.autoclear import auto_clean
from TusharMusic.utils.thumbnails import gen_thumb
from strings import get_string

# ... (အပေါ်ပိုင်း code များ အတူတူပင်)

    async def stream_call(self, link):
        assistant = await group_assistant(self, config.LOG_GROUP_ID)
        await assistant.join_group_call(
            config.LOG_GROUP_ID,
            AudioVideoPiped(link),
        )
        await asyncio.sleep(0.2)
        await assistant.leave_group_call(config.LOG_GROUP_ID)

    async def join_call(self, chat_id: int, original_chat_id: int, link, video: Union[bool, str] = None, image: Union[bool, str] = None):
        assistant = await group_assistant(self, chat_id)
        language = await get_lang(chat_id)
        _ = get_string(language)
        
        stream = (
            AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo())
            if video else AudioPiped(link, audio_parameters=HighQualityAudio())
        )
        
        try:
            await assistant.join_group_call(chat_id, stream)
        except NoActiveGroupCall:
            raise AssistantErr(_["call_8"])
        except AlreadyJoinedError:
            raise AssistantErr(_["call_9"])
        except TelegramServerError:
            raise AssistantErr(_["call_10"])
        await add_active_chat(chat_id)
        await music_on(chat_id)
        if video:
            await add_active_video_chat(chat_id)
        if await is_autoend():
            counter[chat_id] = {}
            users = len(await assistant.get_participants(chat_id))
            if users == 1:
                autoend[chat_id] = datetime.now() + timedelta(minutes=1)

# ... (ကျန်သည့် function များ အတူတူပင်)

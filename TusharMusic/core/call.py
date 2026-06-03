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

autoend = {}
counter = {}

async def _clear_(chat_id):
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)

class Call(PyTgCalls):
    def __init__(self):
        # Session အားလုံးကို Initialize လုပ်ခြင်း
        self.one = PyTgCalls(Client("TusharAssistant1", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING1)), cache_duration=100)
        self.two = PyTgCalls(Client("TusharAssistant2", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING2)), cache_duration=100)
        self.three = PyTgCalls(Client("TusharAssistant3", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING3)), cache_duration=100)
        self.four = PyTgCalls(Client("TusharAssistant4", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING4)), cache_duration=100)
        self.five = PyTgCalls(Client("TusharAssistant5", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING5)), cache_duration=100)

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            await _clear_(chat_id)
            await assistant.leave_group_call(chat_id)
        except: pass

    async def stream_call(self, link):
        assistant = await group_assistant(self, config.LOG_GROUP_ID)
        await assistant.join_group_call(config.LOG_GROUP_ID, AudioVideoPiped(link))
        await asyncio.sleep(0.2)
        await assistant.leave_group_call(config.LOG_GROUP_ID)

    async def join_call(self, chat_id: int, original_chat_id: int, link, video: Union[bool, str] = None):
        assistant = await group_assistant(self, chat_id)
        stream = AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo()) if video else AudioPiped(link, audio_parameters=HighQualityAudio())
        try:
            await assistant.join_group_call(chat_id, stream)
        except (NoActiveGroupCall, AlreadyJoinedError, TelegramServerError):
            raise AssistantErr("Call Error")
        await add_active_chat(chat_id)
        await music_on(chat_id)
        if video: await add_active_video_chat(chat_id)

    async def start(self):
        LOGGER(__name__).info("Starting PyTgCalls Client...")
        if config.STRING1: await self.one.start()
        if config.STRING2: await self.two.start()
        if config.STRING3: await self.three.start()
        if config.STRING4: await self.four.start()
        if config.STRING5: await self.five.start()

Tushar = Call()

import asyncio
import sys

# 1. Event Loop အသစ်ကို အတင်းဖန်တီးပြီး အသက်သွင်းခြင်း
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# 2. uvloop ကို သုံးချင်ပါက Policy ကို အခုမှ သတ်မှတ်ပါ
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass # uvloop မရှိပါကလည်း error မတက်စေရန်

# 3. Loop အဆင်သင့်ဖြစ်မှပဲ Tushar နဲ့ တခြား class တွေကို Import လုပ်ပါ
from TusharMusic.core.bot import Tushar
from TusharMusic.core.dir import dirr
from TusharMusic.core.git import git
from TusharMusic.core.userbot import Userbot
from TusharMusic.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

# Bot ကို စတင်ခြင်း
app = Tushar()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

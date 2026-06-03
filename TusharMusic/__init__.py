import asyncio
import uvloop

# Event Loop ကို အရင်ဆုံး စတင်သတ်မှတ်ပေးပါ
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# ပြီးမှ ကျန်တဲ့ Import များကို ဆက်ရေးပါ
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

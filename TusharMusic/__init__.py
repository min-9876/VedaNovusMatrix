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

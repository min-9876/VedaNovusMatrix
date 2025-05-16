from TusharMusic.core.bot import Netflix
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


Telegram = TeleAPI()
YouTube = YouTubeAPI()

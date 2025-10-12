from ASTA.core.bot import ASTA
from ASTA.core.dir import dirr
from ASTA.core.git import git
from ASTA.core.userbot import Userbot
from ASTA.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from ASTA.core.bot import ASTA
from ASTA.misc import dbb, heroku
from .logging import LOGGER

# Essential startup tasks
dbb()
heroku()

# Initialize main bot instance
app = ASTA()

# Lazy load heavy modules only when accessed
class LazyAPIs:
    _safone_api = None
    _userbot = None

    @property
    def api(self):
        if self._safone_api is None:
            from SafoneAPI import SafoneAPI
            self._safone_api = SafoneAPI()
        return self._safone_api

    @property
    def userbot(self):
        if self._userbot is None:
            from ASTA.core.userbot import Userbot
            self._userbot = Userbot()
        return self._userbot

apis = LazyAPIs()

# Lazy load platform APIs
class Platforms:
    _apple = None
    _carbon = None
    _soundcloud = None
    _spotify = None
    _resso = None
    _telegram = None
    _youtube = None

    @property
    def Apple(self):
        if self._apple is None:
            from .Apple import AppleAPI
            self._apple = AppleAPI()
        return self._apple

    @property
    def Carbon(self):
        if self._carbon is None:
            from .Carbon import CarbonAPI
            self._carbon = CarbonAPI()
        return self._carbon

    @property
    def SoundCloud(self):
        if self._soundcloud is None:
            from .Soundcloud import SoundAPI
            self._soundcloud = SoundAPI()
        return self._soundcloud

    @property
    def Spotify(self):
        if self._spotify is None:
            from .Spotify import SpotifyAPI
            self._spotify = SpotifyAPI()
        return self._spotify

    @property
    def Resso(self):
        if self._resso is None:
            from .Resso import RessoAPI
            self._resso = RessoAPI()
        return self._resso

    @property
    def Telegram(self):
        if self._telegram is None:
            from .Telegram import TeleAPI
            self._telegram = TeleAPI()
        return self._telegram

    @property
    def YouTube(self):
        if self._youtube is None:
            from .YouTube import YouTubeAPI
            self._youtube = YouTubeAPI()
        return self._youtube

platforms = Platforms()

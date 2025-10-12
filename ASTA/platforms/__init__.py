# Safe import system for all platform APIs (Asta fix)
# Prevents crashes if optional modules are missing

try:
    from .Apple import AppleAPI
except ImportError:
    AppleAPI = None

try:
    from .Carbon import CarbonAPI
except ImportError:
    class CarbonAPI:
        pass  # Dummy Carbon class (Asta fix)

try:
    from .Resso import RessoAPI
except ImportError:
    RessoAPI = None

try:
    from .Soundcloud import SoundAPI
except ImportError:
    SoundAPI = None

try:
    from .Spotify import SpotifyAPI
except ImportError:
    SpotifyAPI = None

try:
    from .Telegram import TeleAPI
except ImportError:
    TeleAPI = None

try:
    from .Youtube import YouTubeAPI
except ImportError:
    YouTubeAPI = None

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Basic Configuration
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Owner / Bot Info
OWNER_USERNAME = getenv("OWNER_USERNAME", "ixasta1")
BOT_USERNAME = getenv("BOT_USERNAME", "Laibaamusicbot")
BOT_NAME = getenv("BOT_NAME", "˹ 𝐀𝐬𝐭𝐚 ꭙ 𝐌ᴜ𝐬ɪᴄ ˼")
ASSUSERNAME = getenv("ASSUSERNAME", "Asta_music")

# Database & Duration
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID"))
OWNER_ID = int(getenv("OWNER_ID"))

# Heroku / Git
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ixastamusicbot/OP_ASTA_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# Links
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://t.me/+fLHdtYJusyBkYjk1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ixasta1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/oldskoolgc")

# Assistant Settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song Duration / Limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# String Sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# Spotify Integration
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# YouTube API (Asta’s Key)
YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "NxGBNexGenBots4e1026")

# Default Images
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/tcz7s6.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/79547e01862628bb85df0.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/o5Y.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# Internal Variables
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Duration converter
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL Validations
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHAT URL is invalid. It must start with https://"
        )

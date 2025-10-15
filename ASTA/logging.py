import logging
from logging import Logger, StreamHandler
from logging.handlers import RotatingFileHandler

# ✅ Fast & non-blocking logger setup
def setup_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.hasHandlers():
        # Console handler
        console_handler = StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # Rotating file handler (prevents large log files)
        file_handler = RotatingFileHandler(
            "asta.log", maxBytes=5_000_000, backupCount=3
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


# ✅ Mute unnecessary logs from heavy libraries
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


# ✅ Use this anywhere: LOGGER = get_logger(__name__)
def get_logger(name: str = "ASTA") -> Logger:
    return setup_logger(name)


# ✅ Default main logger
LOGGER = get_logger("ASTA")

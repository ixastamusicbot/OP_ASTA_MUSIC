import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - import logging
from logging import Logger, StreamHandler, FileHandler
from logging.handlers import RotatingFileHandler

# Fast non-blocking logger setup
def setup_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.hasHandlers():
        # Stream handler (console)
        stream_handler = StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(
            logging.Formatter("[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
                              datefmt="%d-%b-%y %H:%M:%S")
        )
        logger.addHandler(stream_handler)

        # Rotating file handler (non-blocking, avoids huge log file)
        file_handler = RotatingFileHandler("log.txt", maxBytes=5_000_000, backupCount=3)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(
            logging.Formatter("[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
                              datefmt="%d-%b-%y %H:%M:%S")
        )
        logger.addHandler(file_handler)

    return logger

# Reduce noise from heavy libraries
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

LOGGER = setup_loggerimport logging
from logging import Logger, StreamHandler, FileHandler
from logging.handlers import RotatingFileHandler

# Fast non-blocking logger setup
def setup_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.hasHandlers():
        # Stream handler (console)
        stream_handler = StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(
            logging.Formatter("[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
                              datefmt="%d-%b-%y %H:%M:%S")
        )
        logger.addHandler(stream_handler)

        # Rotating file handler (non-blocking, avoids huge log file)
        file_handler = RotatingFileHandler("log.txt", maxBytes=5_000_000, backupCount=3)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(
            logging.Formatter("[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
                              datefmt="%d-%b-%y %H:%M:%S")
        )
        logger.addHandler(file_handler)

    return logger

# Reduce noise from heavy libraries
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

LOGGER = setup_logger

import logging
from logging import Logger, StreamHandler
from logging.handlers import RotatingFileHandler

# Function to setup fast, non-blocking logger
def setup_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.hasHandlers():
        # Console handler
        console_handler = StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
                datefmt="%d-%b-%y %H:%M:%S"
            )
        )
        logger.addHandler(console_handler)

        # Rotating file handler (prevents huge log files)
        file_handler = RotatingFileHandler(
            "log.txt", maxBytes=5_000_000, backupCount=3
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
                datefmt="%d-%b-%y %H:%M:%S"
            )
        )
        logger.addHandler(file_handler)

    return logger

# Reduce noise from heavy libraries
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

# LOGGER function to use in all modules
LOGGER = lambda name: setup_logger(name)

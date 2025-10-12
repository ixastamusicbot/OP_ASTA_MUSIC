import os
import asyncio
from ..logging import LOGGER

logger = LOGGER(__name__)

async def clean_images():
    """Remove image files asynchronously"""
    try:
        files = os.listdir()
        tasks = []
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                # Use asyncio.to_thread to make blocking IO async
                tasks.append(asyncio.to_thread(os.remove, file))
        if tasks:
            await asyncio.gather(*tasks)
    except Exception as e:
        logger.info(f"Error cleaning images: {e}")

async def ensure_dirs():
    """Create required directories safely"""
    for folder in ["downloads", "cache"]:
        try:
            if not os.path.exists(folder):
                await asyncio.to_thread(os.mkdir, folder)
        except Exception as e:
            logger.info(f"Error creating directory {folder}: {e}")

async def dirr_async():
    await clean_images()
    await ensure_dirs()
    logger.info("Directories Updated.")

def dirr():
    """Wrapper to run async directory setup safely"""
    try:
        asyncio.get_event_loop().run_until_complete(dirr_async())
    except RuntimeError:
        # If event loop is already running
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(dirr_async())

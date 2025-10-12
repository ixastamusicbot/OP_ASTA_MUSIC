from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.clients = []
        # Prepare client sessions dynamically
        strings = [
            config.STRING1, config.STRING2, config.STRING3,
            config.STRING4, config.STRING5
        ]
        for idx, session in enumerate(strings, start=1):
            if session:
                client = Client(
                    name=f"ASTAAss{idx}",
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=str(session),
                    no_updates=True
                )
                self.clients.append(client)

    async def start(self):
        logger = LOGGER(__name__)
        logger.info("Starting Assistants...")
        for idx, client in enumerate(self.clients, start=1):
            try:
                await client.start()
                # Join required chats safely
                for chat in ["ixasta1", "+wPjAlUcObehiZDM1"]:
                    try:
                        await client.join_chat(chat)
                    except:
                        pass
                assistants.append(idx)
                # Send log message safely
                try:
                    await client.send_message(config.LOGGER_ID, "Assistant Started")
                except:
                    logger.error(
                        f"Assistant Account {idx} failed to access the log group. Make sure it is added and promoted as admin!"
                    )
                    exit()
                # Store IDs and names
                client.id = client.me.id
                client.name = client.me.mention
                client.username = client.me.username
                assistantids.append(client.id)
                logger.info(f"Assistant {idx} Started as {client.name}")
            except Exception as e:
                logger.error(f"Failed to start Assistant {idx}: {e}")

    async def stop(self):
        logger = LOGGER(__name__)
        logger.info("Stopping Assistants...")
        for client in self.clients:
            try:
                await client.stop()
            except:
                pass

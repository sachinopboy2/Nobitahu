import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class NobitaBot(Client):
    def __init__(self):
        super().__init__(
            name="NobitaMusic",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
        )

    async def start(self):
        await super().start()
        print("Nobita Music Bot is Online! ✅")

    async def stop(self):
        await super().stop()
        print("Bot Stopped! 🛑")

if __name__ == "__main__":
    app = NobitaBot()
    app.run()
  

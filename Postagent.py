import time
import asyncio
from telegram import Bot

class TelegramAgent:
    def __init__(self, api_token, chat_id):
        self.bot = Bot(token=api_token)
        self.chat_id = chat_id

    async def post_message(self, message):
        await self.bot.send_message(chat_id=self.chat_id, text=message)
        print(f"Posted to Telegram: {message}")

if __name__ == "__main__":
    API_TOKEN = "7728390972:AAE7VKoq5J-lzuUnuC9jx9QLF-PLB5rSJ-g"  # Your bot token
    CHAT_ID = "6698380531"  # Your chat ID

    agent = TelegramAgent(API_TOKEN, CHAT_ID)

    async def main():
        while True:
            await agent.post_message("Hello! This is an automated post every 2 minutes.")
            await asyncio.sleep(120)  # Wait for 2 minutes

    asyncio.run(main())
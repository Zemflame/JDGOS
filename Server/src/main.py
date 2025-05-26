import asyncio
import discord
import uvicorn
from fastapi import FastAPI

def loadBotToken():
    with open("token.txt", "r") as f:
        return f.read()

botClient: discord.Client | None = None
botToken: str = loadBotToken()

async def startBot():
    global botClient

    class BotClient(discord.Client):
        async def on_ready(self):
            print(f'Logged on as {self.user}!')

        async def on_message(self, message: discord.Message):
            print(f'Message from {message.author}: {message.content}')

            for attachment in message.attachments:
                if attachment.filename.lower().endswith(".gif"):
                    print("User uploaded file containing GIF.")
            
            for embed in message.embeds:
                if embed.type == "gifv":
                    print("GIF detected in gifv embed (e.g., Tenor).")
                if embed.type == "image" and isinstance(embed.url, str) and embed.url.lower().endswith(".gif"):
                    print("GIF detected in image embed (CDN-hosted).")

    intents = discord.Intents.default()
    intents.message_content = True

    botClient = BotClient(intents=intents)
    await botClient.start(botToken)

async def startAPIServer():
    app = FastAPI()

    @app.get("/test")
    async def test():
        return {"message": "Hello from server!"}

    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        startAPIServer(),
        startBot()
    )
if __name__ == "__main__":
    asyncio.run(main())

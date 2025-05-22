import discord

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')

def loadBotToken():
    with open("token.txt", "r") as f:
        return f.read()

botClient: BotClient | None = None
botToken: str = loadBotToken()

def setupBot():
    global botClient

    intents = discord.Intents.default()
    intents.message_content = True

    botClient = BotClient(intents=intents)
    botClient.run(botToken)

def main():
    setupBot()

if __name__ == "__main__":
    main()
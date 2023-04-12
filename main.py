# Sanware Framework MK III - Branch 'Carter-Discord Boilerplate'

# Boilerplate for linking Discord bot with a Carter API. Written by TheMechanic57.

# Load packages.

# All pip installs required:
### pip install nextcord
### pip install googletrans==3.1.0a0
### pip install python-dotenv
### pip install requests

import os
import nextcord as discord
from carter import *
from googletrans import Translator
from dotenv import load_dotenv

intents = discord.Intents.all()
client = discord.Client(intents=intents)

load_dotenv()
APIkey = os.getenv("CARTER_API_KEY") # In .env add a variable called: CARTER_API_KEY = "Your API Key"
DiscordAPI = os.getenv("DISCORD_API_KEY") # In .env add a variable called: DISCORD_API_KEY = "Your API Key"

RawUIName = "Holo"
translator = Translator()

print(f"{RawUIName} is Online...")

# Program

@client.event
async def on_message(message):
    # Script is below.

    if message.author == client.user:
        return

    User = message.author
    UserNick = User.nick
    sentence = message.content
    sentence = sentence.lower()
    UIName = RawUIName.lower()

    if UIName in sentence:
        if not sentence.startswith(UIName):
            try:
                sentence = translator.translate(sentence, src=translator.detect(sentence).lang, dest='de').text
            except Exception as e:
                await message.channel.send("Error translating input text: " + str(e))
                return

        ResponseOutput = SendToCarter(sentence, User, APIkey)
        print(f"Carter API says: {ResponseOutput}")

        if not ResponseOutput.startswith(UIName):
            try:
                ResponseOutput = translator.translate(ResponseOutput, src=translator.detect(ResponseOutput).lang, dest='de').text
            except Exception as e:
                await message.channel.send("Error translating response text: " + str(e))
                return
            
        await message.channel.send(f"{ResponseOutput}")
        print(f"{UserNick}: {sentence}\n{UIName}: {ResponseOutput}")
    else:
        pass

client.run(DiscordAPI)
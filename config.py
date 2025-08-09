import discord
import pytz
import platform
import datetime
import os
import asyncio
from discord.ext import tasks
from discord.ext import commands
from colorama import Back, Fore, Style
from dotenv import load_dotenv




load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)




@client.event
async def on_ready():
    cest_tz = pytz.timezone('Europe/Paris')
    current_time = datetime.datetime.now(tz=cest_tz)
    prfx = (Back.BLACK + Fore.GREEN + current_time.strftime("%H%M%S") + Back.RESET + Fore.WHITE + Style.BRIGHT + Fore.CYAN + Fore.MAGENTA )
    print(f"{prfx} Logged as {Fore.YELLOW}{client.user.name}")
    print(f"{prfx} Bot ID {Fore.YELLOW}{client.user.id}")
    print(f"{prfx} Discord Version {Fore.YELLOW}{discord.__version__}")
    print(f"{prfx} Python Version {Fore.YELLOW}{str(platform.python_version())}")
    print(f"{prfx} Succesfully logged in as APD {Fore.CYAN}")
    activity = discord.Activity(type=discord.ActivityType.listening, name=f"main.py")
    await client.change_presence(activity=activity)
    await client.tree.sync() 




async def load():
    for folder in ["Prefix", "Slash"]:
        for filename in os.listdir(f"./{folder}"):
            if filename.endswith(".py"):
                await client.load_extension(f"{folder}.{filename[:-3]}")
                print(f"{filename} loaded from {folder} folder.")


async def main():
    async with client:
        await load()
        await client.start(DISCORD_TOKEN)


asyncio.run(main())




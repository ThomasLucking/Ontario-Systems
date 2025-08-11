import discord
from discord.ext import commands

class say(commands.Cog):
    def __init__(self, client):
        self.client = client



async def setup(client):
    await client.add_cog(say(client))

import discord
from discord.ext import commands

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client



async def setup(client):
    await client.add_cog(kick(client))

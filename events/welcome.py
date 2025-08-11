import discord
from discord.ext import commands

class welcomemessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("welcome.py is Ready!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1403401152548048913
        send_channel = self.client.get_channel(channel_id)

        welcomemessage = (
    f"<:Welcome:1403810469881577623> Welcome {member.mention} to <:Ontario:1403502648321245265>Ontario Provincial Roleplay! "
    f"We are now at {member.guild.member_count} members."
    )

        
        
        await send_channel.send(welcomemessage)

    

async def setup(client):
    await client.add_cog(welcomemessage(client))
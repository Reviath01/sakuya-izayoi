import discord 
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation commands are loaded!')

    @commands.command(brief="Ban the user", description="Allow's you to ban the user")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member:discord.User = None, reason = None):
        if member == None:
            await ctx.send('You need to mention someone.')
            return
        if member == ctx.message.author:
            await ctx.send('You can\'t ban yourself.')
            return
        if reason == None:
            reason = "Unspecified"
        message = f"You have been banned from {ctx.guild.name} for {reason}."
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} is banned!")
        
def setup(client):
    client.add_cog(Moderation(client))
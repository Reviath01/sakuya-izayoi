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
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} is banned!")

    @commands.command(brief="Kick the user", description="Allow's you to kick the user")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member:discord.User = None, reason = None):
        if member == None:
            await ctx.send('You need to mention someone.')
            return
        if member == ctx.message.author:
            await ctx.send('You can\'t kick yourself.')
            return
        if reason == None:
            reason = "Unspecified"
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f"{member} is kicked!")

    @commands.command(brief="Unban the user", description="Unban's the user")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member = None):
        if member == None:
            await ctx.send('You need to specify a ID')
            return
        user = await self.client.fetch_user(member)
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned <@{user.id}>')
        return

    @commands.command(brief="Start a vote", description="Start a vote")
    @commands.has_permissions(manage_messages = True)
    async def start_vote(self, ctx, *, message = None):
        if message == None:
            await ctx.send('You need to say why are you starting a vote')
            return
        voteembed = discord.Embed(colour=discord.Colour.blue(), title=f"Vote started (by {ctx.author.display_name})", description=message)
        msg = await ctx.send(embed = voteembed)
        emoji = '\N{THUMBS UP SIGN}'
        emoji2 ='\N{THUMBS DOWN SIGN}'
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)

    @commands.command(brief="Deletes messages", description="Deletes messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Cleared {amount} messages.')

def setup(client):
    client.add_cog(Moderation(client))

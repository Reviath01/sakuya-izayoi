import discord 
from discord.ext import commands

class User(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('User commands are loaded!')

    @commands.command(brief="Send's latency of bot", description="Send's latency of bot")
    async def ping(self, ctx):
        await ctx.send(f'Pong! {self.client.latency * 1000}')

    @commands.command(brief="Send's user information", description="Send's information about user (if you don't mention anyone, it will show yours)")
    async def whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role.mention for role in member.roles[1:]]
        roles.append('@everyone')
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Roles:", value="".join(roles))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command(brief="Fetch the profile picture of a user", description="Fetch the profile picture of a user", aliases=["pfp", "profile", "pp"])
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        messageembed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at, title=f"Avatar of {member}")
        messageembed.set_image(url=member.avatar_url)
        await ctx.send(embed=messageembed)

    @commands.command(brief="Invite me!", description="My invite link")
    async def invite(self, ctx):
        inviteembed = discord.Embed(colour=discord.Colour.red(), description="[Click here to invite me!](https://discordapp.com/oauth2/authorize?client_id=808385152601817169&scope=bot&permissions=8)")
        await ctx.send(embed=inviteembed)

def setup(client):
    client.add_cog(User(client))
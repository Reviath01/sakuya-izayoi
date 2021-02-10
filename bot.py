import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = "!")
status = cycle(['Leviathan Dev Team', 'Reviath'])

@client.event
async def on_ready():
    change_status.start()
    print(client.user.display_name + '#' + client.user.discriminator + ' is ready!')

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(brief="Author command", description="Author command")
async def load(ctx, extension):
    if str(ctx.author.id) == "770218429096656917":
        client.load_extension(f'cogs.{extension}')
        await ctx.send(':+1:')
    else:
        await ctx.send('This command is only for my author')

@client.command(brief="Author command", description="Author command")
async def unload(ctx, extension):
    if str(ctx.author.id) == "770218429096656917":
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(':+1:')
    else:
        await ctx.send('This command is only for my author')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import sys
import json

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)
status = cycle(['Prefix: !', 'Reviath'])

@client.event
async def on_command_error(ctx, error):
    log = client.get_channel(790640302452375562)
    await ctx.send(error)
    await log.send(f'Error on server `{ctx.guild.name}` \n{error}')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_ready():
    log = client.get_channel(790640302452375562)
    change_status.start()
    print(client.user.display_name + '#' + client.user.discriminator + ' is ready!')
    await log.send('I am ready to use!')

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(brief="Shows my author", description="Shows my author")
async def author(ctx):
    authorembed = discord.Embed(description="My Author: \n<@!770218429096656917> ([Reviath#0001](https://discord.com/users/770218429096656917))", colour=discord.Colour.purple())
    await ctx.send(embed = authorembed)

@client.command(brief="Author command", description="Author command", hidden = True)
async def load(ctx, extension):
    if str(ctx.author.id) == "770218429096656917":
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded cogs.{extension}.')
    else:
        await ctx.send('This command is only for my author.')

@client.command(brief="Author command", description="Author command", hidden = True)
async def unload(ctx, extension):
    if str(ctx.author.id) == "770218429096656917":
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded cogs.{extension}.')
    else:
        await ctx.send('This command is only for my author.')

@client.command(brief="Author command", description="Author command", hidden = True)
async def reload(ctx, extension):
    if str(ctx.author.id) == "770218429096656917":
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded cogs.{extension}.')
    else:
        await ctx.send('This command is only for my author')

@client.command(brief="Author command", description="Author command", hidden = True)
async def shutdown(ctx):
    if str(ctx.author.id) == "770218429096656917":
        await ctx.send('Shuting down!')
        await client.logout()
    else:
        await ctx.send('This command is only for my author.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@client.command(brief="Author command", description="Author command", hidden = True)
async def restart(ctx):
    if str(ctx.author.id) == "770218429096656917":
        await ctx.send("Restarting...")
        log = client.get_channel(790640302452375562)
        await log.send('Restarting...')
        restart_program()
    else:
        await ctx.send('This command is only for my author.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')

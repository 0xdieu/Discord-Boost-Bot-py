import discord 
from discord.ext import commands, tasks
import os
import json
from discord import Permissions
intents = discord.Intents.all()

client = commands.Bot(command_prefix="+",help_command= None,intents=intents)
def load_command():
    commandnb = 0
    for filename in os.listdir('./command'):

        if filename.endswith('.py'):
            client.load_extension(f'command.{filename[:-3]}')
            
            
    print(f"Tout les command on été load avec succes\nNombre Command {commandnb}")
def unload_command():
    commandnb = 0
    for filename in os.listdir('./command'):
        commandnb = commandnb+ 1
        if filename.endswith('.py'):
            client.unload_extension(f'command.{filename[:-3]}')
def load_command_version(version):
    commandnb = 0
    for filename in os.listdir(f'./command/v{version}'):
        commandnb = commandnb+ 1
        if filename.endswith('.py'):
            client.load_extension(f'command.{filename[:-3]}')
def unload_command_version(version):
    commandnb = 0
    for filename in os.listdir(f'./command/v{version}'):
        commandnb = commandnb+ 1
        if filename.endswith('.py'):
            client.unload_extension(f'command.{filename[:-3]}')
load_command()
@client.command()
async def reload(ctx):
    await ctx.send("Les command on été reload")
    unload_command()
    load_command()
@client.event
async def on_ready():
    print(client.user.name)
    game = discord.Game(name=f"Boost Bot v2")
    await client.change_presence(status=discord.Status.online, activity=game)
client.run("bot token")

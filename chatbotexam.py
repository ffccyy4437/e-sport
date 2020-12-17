import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)


async def on_ready():
    print('bot is here for ready.')


async def on_member_join(member):
    print(f'{member} has joined a server.')


async def on_member_remove(member):
    print(f'{member} left the server.')


async def add(ctx,a:float):
    await ctx.send(a)

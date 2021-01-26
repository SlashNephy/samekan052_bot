import json
import requests
import discord

from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix='s!', intents=discord.Intents.all())
slash = SlashCommand(bot, auto_register=True)

api_url = 'https://samekan052.vercel.app/api'

headers = {"content-type": "application/json"}

desc = 'samekan.work'

@slash.slash(name='samekan', description=desc)
async def _samekan(ctx: SlashContext):
    r = requests.get(api_url, headers=headers)
    samekanized = r.json()['sentence']
    await ctx.send(content=samekanized)

bot.run('')

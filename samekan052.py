import json
import os
import urllib.request
from asyncio import TimeoutError

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_actionrow, create_button, wait_for_component

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="s!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

def get_api():
    headers = {
        "User-Agent": "samekan052_bot (+https://github.com/SlashNephy/samekan052_bot)",
        "Content-Type": "application/json"
    }
    request = urllib.request.Request("https://samekan052.vercel.app/api", headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read().decode()
        return json.loads(content)

def get_random_sentence():
    api = get_api()
    return api["sentence"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

    activity = discord.Game(name="Apex Legends")
    await bot.change_presence(activity=activity)

@slash.slash(name="samekan", description="さめちゃんを呼び寄せます。")
async def on_samekan_command(ctx: SlashContext):
    action_row = create_actionrow(
        create_button(
            style=ButtonStyle.primary,
            emoji="\U0001F504",
            label="やりなおし"
        )
    )

    await ctx.send(
        content=get_random_sentence(),
        components=[action_row]
    )

    while True:
        button_ctx = await wait_for_component(bot, components=action_row)
        await button_ctx.edit_origin(content=get_random_sentence())

bot.run(TOKEN)

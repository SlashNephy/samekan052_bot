import json
import os
import urllib.request

import discord
from discord.ext import commands
from discord_slash import ComponentContext, SlashCommand, SlashContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_actionrow, create_button

TOKEN = os.getenv("TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://samekan.starry.blue")
COMMAND = os.getenv("COMMAND", "samekan")
DESCRIPTION = os.getenv("DESCRIPTION")
GAME = os.getenv("GAME", "Apex Legends")


bot = commands.Bot(command_prefix="s!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

def get_api():
    headers = {
        "User-Agent": "samekan052_bot (+https://github.com/SlashNephy/samekan052_bot)",
        "Content-Type": "application/json"
    }
    request = urllib.request.Request(f"{API_BASE_URL}/api", headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read().decode()
        return json.loads(content)

def get_random_sentence():
    api = get_api()

    return api["sentence"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

    activity = discord.Game(name=GAME)
    await bot.change_presence(activity=activity)

@slash.slash(name=COMMAND, description=DESCRIPTION)
async def on_command(ctx: SlashContext):
    action_row = create_actionrow(
        create_button(
            custom_id="on_redo",
            style=ButtonStyle.primary,
            emoji="\U0001F504",
            label="やりなおし"
        ),
        create_button(
            custom_id="on_finalize",
            style=ButtonStyle.secondary,
            emoji="\U00002705",
            label="完成"
        )
    )

    await ctx.send(
        content=get_random_sentence(),
        components=[action_row]
    )

@slash.component_callback()
async def on_redo(ctx: ComponentContext):
    await ctx.edit_origin(content=get_random_sentence())

@slash.component_callback()
async def on_finalize(ctx: ComponentContext):
    await ctx.edit_origin(components=[])

bot.run(TOKEN)

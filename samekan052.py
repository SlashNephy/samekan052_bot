import json
import os
import urllib.request

import discord
from discord.ext import commands
from discord_slash import ComponentContext, SlashCommand, SlashContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_actionrow, create_button

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
            custom_id="redo",
            style=ButtonStyle.primary,
            emoji="\U0001F504",
            label="やりなおし"
        ),
        create_button(
            custom_id="finalize",
            style=ButtonStyle.danger,
            emoji="<:samekan_sick:708317022093574155>",
            label="完成"
        )
    )

    await ctx.send(
        content=get_random_sentence(),
        components=[action_row]
    )

@slash.component_callback()
async def redo(ctx: ComponentContext):
    await ctx.edit_origin(content=get_random_sentence())

@slash.component_callback()
async def finalize(ctx: ComponentContext):
    await ctx.edit_origin(components=[])

bot.run(TOKEN)

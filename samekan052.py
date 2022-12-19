import json
import os
import urllib.request

import interactions


TOKEN = os.getenv("TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://samekan052.vercel.app")
COMMAND = os.getenv("COMMAND", "samekan")
DESCRIPTION = os.getenv("DESCRIPTION", "さめちゃんを呼び寄せます。")
GAME = os.getenv("GAME")

bot = interactions.Client(token=TOKEN)
redo_button = interactions.Button(
    custom_id="on_redo",
    style=interactions.ButtonStyle.PRIMARY,
    emoji=interactions.Emoji(name="\U0001F504"),
    label="やりなおし",
)
complete_button = interactions.Button(
    custom_id="on_finalize",
    style=interactions.ButtonStyle.SECONDARY,
    emoji=interactions.Emoji(name="\U00002705"),
    label="完成",
)
action_row = interactions.ActionRow.new(redo_button, complete_button)


def get_random_sentence():
    headers = {
        "User-Agent": "samekan052_bot (+https://github.com/SlashNephy/samekan052_bot)",
        "Content-Type": "application/json"
    }
    request = urllib.request.Request(f"{API_BASE_URL}/api", headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read().decode()
        payload = json.loads(content)
        return payload["sentence"]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.me}!")

    if GAME:
        presence = interactions.ClientPresence(
            activities=[
                interactions.PresenceActivity(name=GAME),
            ],
        )
        await bot.change_presence(presence)


@bot.command(name=COMMAND, description=DESCRIPTION)
async def on_command(ctx: interactions.CommandContext):
    await ctx.send(
        content=get_random_sentence(),
        components=action_row,
    )


@bot.component(redo_button)
async def on_redo(ctx: interactions.ComponentContext):
    await ctx.edit(content=get_random_sentence())


@bot.component(complete_button)
async def on_complete(ctx: interactions.ComponentContext):
    await ctx.edit(components=[])


bot.start()

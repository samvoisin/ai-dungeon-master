import logging
import os
from pathlib import Path

import discord

from aidm import AIDungeonMaster

DEFAULT_PROMPT_PATH = Path("prompts/aidm-system-prompt.txt")
DISCORD_TOKEN = os.environ["AI_DM_BOT_KEY"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


def initialize_ai_dungeon_master(
    system_prompt_path: Path = DEFAULT_PROMPT_PATH,
) -> AIDungeonMaster:
    aidm = AIDungeonMaster(system_prompt_path=system_prompt_path)
    # aidm = AIDungeonMaster.construct_from_history(
    #     Path("lmop-system-prompt.txt"), Path("conversation_history.json")
    # )
    return aidm


async def handle_message(message: discord.Message) -> None:
    if message.author == client.user or message.channel.name != "aidm":
        return

    if message.content == "#save":
        # aidm.save_conversation_history()
        await message.channel.send("Conversation history saved")
        return

    logging.info(
        f"author: {message.author}\nchannel: {message.channel}\ncontent: {message.content}\nembeds: {message.embeds}"
    )

    ai_message = aidm.query_model(message.content)
    await message.channel.send(ai_message)


@client.event
async def on_ready():
    global aidm
    aidm = initialize_ai_dungeon_master()
    logging.info(f"{client.user} is now running")


@client.event
async def on_message(message: discord.Message) -> None:
    logging.info(f"Message received from user: {message}")
    await handle_message(message)


def run_dm_bot():
    client.run(DISCORD_TOKEN)

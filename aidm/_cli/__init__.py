from pathlib import Path
from typing import Union

import click

from aidm.discord_bot import run_dm_bot


@click.group()
def cli():
    """
    AI DM command line interface.
    """
    pass

@cli.command()
@click.option('--system-prompt-path', default='prompts/aidm-system-prompt.txt', help='Path to the system prompt file.')
@click.option('--history-path', default=None, help='Path to the conversation history file.')
def run(system_prompt_path: Union[str, Path], history_path: Union[str, Path]):
    """
    Activate the AI Dungeon Master Discord bot.
    """
    system_prompt_path = Path(system_prompt_path)

    if history_path is not None:
        raise NotImplementedError("Loading save files is not implemented yet.")

    run_dm_bot(system_prompt_path=Path(system_prompt_path), history_path=history_path)

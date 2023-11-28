import click

from aidm.discord_bot import run_dm_bot


@click.group()
def cli():
    """
    AI DM command line interface.
    """
    pass

@cli.command()
def run():
    """
    Activate the AI Dungeon Master Discord bot.
    """
    run_dm_bot()

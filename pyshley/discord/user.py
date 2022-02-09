import lightbulb
from pyshley.discord.launch import bot


@bot.command
@lightbulb.command("token", "Uploads a character's token picture.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def uploadToken(ctx: lightbulb.Context) -> None:
    """
    Uploads a character's token picture.

    Regardless of input the token image is reformatted to a 200px square .webp with naming convention
    <ActorName>-token.webp

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    pass


@bot.command
@lightbulb.command("portrait", "Uploads a character's portrait picture.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def uploadPortrait(ctx: lightbulb.Context) -> None:
    """
    Uploads a character's portrait picture.

    Regardless of input the token image is reformatted to a .webp with naming convention
    <ActorName>-portrait.webp

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    pass


@bot.command
@lightbulb.add_checks(lightbulb.dm_only)
@lightbulb.command("password", "Queues a change to the user's password.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def changePassword(ctx: lightbulb.Context) -> None:
    """
    Changes a user's password.

    Changes a user's password.  Queued until server backup.

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    pass

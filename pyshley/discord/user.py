import lightbulb
from pyshley.discord.launch import bot, authorIsGM


@bot.command
@lightbulb.add_checks(lightbulb.Check(authorIsGM))
@lightbulb.command("createUser", "Creates a new FoundryVTT user.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def createUser(ctx: lightbulb.Context) -> None:
    """
    Creates a new FoundryVTT user.

    Creates a new User profile with Player level permissions, generates a temporary password, and notifies the player
    of their updated account.  Queued until server backup.

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    pass


@bot.command
@lightbulb.add_checks(lightbulb.Check(authorIsGM))
@lightbulb.command("createActor", "Creates a new FoundryVTT actor.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def createActor(ctx: lightbulb.Context) -> None:
    """
    Creates a new FoundryVTT Actor.

    Checks if the invoking user has reached their character limit and if not,
    creates a new FoundryVTT Actor and binds it to the invoking user.

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    pass


@bot.command
@lightbulb.add_checks(lightbulb.Check(authorIsGM))
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
@lightbulb.add_checks(lightbulb.Check(authorIsGM))
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

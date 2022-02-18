import lightbulb
from pyshley.discord.launch import bot, isValidAdmin, isValidGM

@bot.command
@lightbulb.add_checks(lightbulb.Check(isValidAdmin))
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
@lightbulb.add_checks(lightbulb.Check(isValidAdmin))
@lightbulb.command("createGM", "Creates a new FoundryVTT game master.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def createGM(ctx: lightbulb.Context) -> None:
    """
    Creates a new FoundryVTT game master.

    Creates a new User profile with Assistant level permissions and generates a temporary password.
    creates gm_<name> folders in Scenes, Actors, Items, Journal, Rollable Tables, and Audio Playlist. Notifies the
    player of their updated account.  Queued until server backup.

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    pass


@bot.command
@lightbulb.add_checks(lightbulb.Check(isValidGM))
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

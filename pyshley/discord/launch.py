import lightbulb
from pyshley.lib.log import logger
from pyshley.lib.config import token, prefix, adminIDList, gmIDList, botChannelList

bot = lightbulb.BotApp(token=token, prefix=prefix)


@lightbulb.Check
def isValidGM(ctx: lightbulb.Context) -> bool:
    """
    Authorizes the execution of a GM level command.

    Checks if the invoking user is in gmIDList and if the channel is in gmChannelList.

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    if not str(ctx.author.id) in gmIDList:
        logger.info(f"Unauthorized user {ctx.author.id} attempted command {ctx.command}")

    if not str(ctx.channel_id) in botChannelList:
        logger.info(f"Authorized user {ctx.author.id} attempted command {ctx.command} in non gm channel {ctx.channel_id}")

    else:
        return True

    # TODO: Delete invoking command
    # TODO: Inform user they aren't authorized
    return False


@lightbulb.Check
def isValidAdmin(ctx: lightbulb.Context) -> bool:
    """
    Authorizes the execution of an Admin level command.

    Checks if the invoking user is in adminIDList.

    Parameters:
    arg1 (Context): The Context that invoked the command.
    """
    if str(ctx.author.id) in adminIDList:
        return True

    # TODO: Delete invoking command
    # TODO: Mention user in botChannel at index 0
    logger.info(f"Unauthorized user {ctx.author.id} attempted command {ctx.command}")
    return False


@lightbulb.Check
def isBotChannel(ctx: lightbulb.Context) -> bool:
    if str(ctx.channel_id) in botChannelList:
        return True

    # TODO: Delete invoking command
    # TODO: Mention user in botChannel at index 0
    logger.info(f"Command {ctx.command} sent to non bot channel {ctx.channel_id}")
    return False


@bot.command
@lightbulb.command("ping", "Checks if Ashley is clocked in.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    if ctx.user.is_bot:
        return

    await ctx.respond("I'm awake!")

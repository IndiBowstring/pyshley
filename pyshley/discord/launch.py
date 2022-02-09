import lightbulb
from pyshley.lib.log import logger
from pyshley.lib.config import discordSettings, gmIDList

bot = lightbulb.BotApp(token=discordSettings['token'], prefix=discordSettings['prefix'])


@lightbulb.Check
def authorIsGM(ctx: lightbulb.Context) -> bool:
    if str(ctx.author.id) in gmIDList:
        return True

    logger.info(f"Unauthorized user {ctx.author.id} attempted command {ctx.command}")
    return False


@bot.command
@lightbulb.command("ping", "Checks if Ashley is clocked in.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    if ctx.user.is_bot:
        return

    await ctx.respond("I'm awake!")

import hikari

from pyshley.discord.checks import *
from pyshley.discord.dice import DicePlugin
from pyshley.lib.config import token, prefix

bot = lightbulb.BotApp(
    token=token,
    prefix=prefix,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(671825516310822959,),
    help_slash_command=True)


bot.add_plugin(DicePlugin)


@bot.command
@lightbulb.add_checks(lightbulb.checks.human_only)
@lightbulb.command("ping", "Checks if Ashley is clocked in.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("I'm awake!")


@bot.command
@lightbulb.add_checks(lightbulb.Check(isValidAdmin))
@lightbulb.command("announce", "Sends a message through Ashley.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def announce(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.event.message.content[10:])
    await ctx.event.message.delete()

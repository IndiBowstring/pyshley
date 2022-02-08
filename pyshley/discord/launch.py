import hikari
from pyshley.lib.config import discordSettings

bot = hikari.GatewayBot(token=discordSettings['token'])


@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    if event.content.startswith("ping"):
        await event.message.respond("Pong!")


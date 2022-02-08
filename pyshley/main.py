from pyshley.discord.launch import bot
from pyshley.lib.log import logger


def main():
    logger.info("Pyshley Discord Bot starting...")
    bot.run()


if __name__ == '__main__':
    main()

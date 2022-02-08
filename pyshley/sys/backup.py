import subprocess


# TODO: delete hint
# The current full container list is pyshley.lib.config.foundrySettings['dockerContainers'].keys()


def dockerStop(containers: list) -> None:
    """
    Stops each listed container.

    Parameters:
    arg1 (list): List of container names.
    """
    pass


def dockerStart(containers: list) -> None:
    """
    Starts each listed container.

    Parameters:
    arg1 (list): List of container names.
    """
    pass


def fullBackup() -> str:
    """
    Performs a full backup of foundry data.

    Deposits Player, World, Module, and Asset data into a .tar.gz within the default backup directory.
    Naming scheme follows: YYMMDD-full.tar.gz

    Returns:
    str: Absolute path to the tarball.
    """
    pass


def playerBackup() -> str:
    """
    Performs a partial backup of player data.

    Deposits Player data into a .tar.gz within the default backup directory.
    Naming scheme follows: YYMMDD-player.tar.gz

    Returns:
    str: Absolute path to the tarball.
    """
    pass


def assetBackup() -> str:
    """
    Performs a partial backup of asset data.

    Deposits Asset data into a .tar.gz within the default backup directory.
    Naming scheme follows: YYMMDD-asset.tar.gz

    Returns:
    str: Absolute path to the tarball.
    """
    pass

def worldBackup() -> str:
    """
    Performs a partial backup of world data.

    Deposits Asset data into a .tar.gz within the default backup directory.
    Naming scheme follows: YYMMDD-world.tar.gz

    Returns:
    str: Absolute path to the tarball.
    """
    pass

def moduleBackup() -> str:
    """
    Performs a partial backup of module data.

    Deposits Asset data into a .tar.gz within the default backup directory.
    Naming scheme follows: YYMMDD-module.tar.gz

    Returns:
    str: Absolute path to the tarball.
    """
    pass
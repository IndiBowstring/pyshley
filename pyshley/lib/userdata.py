import json
import os
from pathlib import Path
from pyshley.lib.log import logger
import lightbulb

from pyshley import ROOT_DIR

userdata = {}


async def reloadUserData(ctx: lightbulb.Context) -> None:
    """
    Reloads the userdata dictionary.

    Fetches updated discord information, loads the userdata dictionary and writes it to file.

    :param ctx: (Context) The Context that invoked the command.
    """
    userdata.clear()
    _request = dict(zip(ctx.get_guild().get_members().keys(), ctx.get_guild().get_members().values()))
    _JSON = await readUserDataJSON()
    for k, v in _request.items():
        if v.is_bot:
            continue
        userdata[k] = {}
        userdata[k]["discord"] = {"id": v.id, "username": v.username, "nickname": v.nickname, "roles": v.role_ids}
        userdata[k]["foundry"] = _JSON[k]["foundry"] if "foundry" in userdata[k].keys() else {"users": []}  # Temporary until FoundryData
        # TODO: Possibly store ticket history in cache?
    await writeUserDataJSON()
    logger.info(f"Reloaded user data")


async def readUserDataJSON() -> dict:
    """
    Reads json files in db/ subdirectory into dictionary.

    Reads each json file in db/ and appends its contents to the return value with a Snowflake key that matches the file
    name without the file extension.

    :returns: out (dict): { discord_snowflake : user_data }
    """
    out = {}
    for fileName in os.listdir(os.path.join(ROOT_DIR, 'db')):
        with open(os.path.join(ROOT_DIR, 'db', fileName), 'r') as file:
            out[Path(fileName).stem] = json.load(file)
    return out


async def writeUserDataJSON() -> None:
    """
    Writes the userdata dictionary to file.

    Writes each entry to the appropriate file named <Snowflake>.json.  If the file does not exist, create it.
    """
    for k, user in userdata.items():
        with open(os.path.join(ROOT_DIR, 'db', str(k) + '.json'), 'w+') as file:
            json.dump(user, file)


class FoundryData:
    def __init__(self):
        self.users = []
        # TODO: users = [userID: {password: "", tokenImg: "path", portraitImg: "path"}]
        # TODO: Serialization for json.dump

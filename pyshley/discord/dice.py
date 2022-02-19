import random
import re
import typing
from itertools import islice

import lightbulb

from pyshley.discord.launch import isBotChannel
from pyshley.lib.utils import clampIfExists

DicePlugin = lightbulb.Plugin("DicePlugin")


class RollPayload:
    def __init__(self, invokingCommand=(), initialRolls=(), processedRolls=()):
        self.invokingCommand: tuple = invokingCommand
        self.initialRolls: tuple = initialRolls
        self.processedRolls: tuple = processedRolls

    def __str__(self):
        return f"RollPayload\n" \
               f"invokingCommand={self.invokingCommand}\n" \
               f"initialRolls={self.initialRolls}\n" \
               f"processedRolls={self.processedRolls}"


@DicePlugin.command
@lightbulb.add_checks(lightbulb.Check(isBotChannel))
@lightbulb.option("roll", "The roll query in ndm format.", required=False, default="1d20")
@lightbulb.command("roll", "The roll query in NdM+p format. Also supports: kh, kl, ro, ra, !")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def roll(ctx: lightbulb.Context) -> None:
    token = tokenize(ctx.options.roll)
    rollResults = processRolls(token)
    displayResults = displayRolls(rollResults)
    await ctx.respond(displayResults)


def tokenize(query: typing.Optional[str]) -> tuple:
    """
    Tokenizes roll query string.

    Defaults to 1d20 on regex match failure, not case-sensitive.

    :param query: (str|None) Raw string input to be tokenized in NdM<cmd>+P format.
    :returns: (N: int, M: int, cmd: str|None, (comparator: str|None, compareValue: int), P: int)
    """
    if query:
        print(query)
        out = re.search(r"^(\d+)?d(\d+)?(kH|kL|ro|ra|!)?([<|>])?(\d+)?([+|-]?\d+)?$", query, re.IGNORECASE)
        if out:
            return (
                clampIfExists(out.groups()[0], 1, 50, 1),
                clampIfExists(out.groups()[1], 1, 100, 20),
                out.groups()[2].lower() if out.groups()[2] else None,
                (
                    out.groups()[3],
                    clampIfExists(out.groups()[4], 0, 50, 0)
                ),
                clampIfExists(out.groups()[5], 0, 1000, 0),
            )
    return 1, 20, None, (None, 0), 0  # Roll default of 1d20


def processRolls(token: tuple) -> RollPayload:
    """
    Calculates roll result.

    Constructs a RollPayload object using tokenized input.

    :param token: (N, M, cmd, (cmp, cmpVal), P) returned from tokenize().
    :returns: (RollPayload): invokingCommand: (), initialRolls: (), processedRolls: ()
    """
    initialRolls = []
    for idx in range(0, token[0]):
        initialRolls.append(random.randint(1, token[1]))

    processedRolls = []
    if token[2] == "kh":
        _initialRolls = initialRolls.copy()  # Preserve order of initial rolls
        _initialRolls.sort()
        processedRolls = list(islice(reversed(_initialRolls), 0, token[3][1]))

    elif token[2] == "kl":
        _initialRolls = initialRolls.copy()  # Preserve order of initial rolls
        _initialRolls.sort()
        processedRolls = list(islice(_initialRolls, 0, token[3][1]))

    elif token[2] == "ro":
        _initialRolls = initialRolls.copy()  # Preserve order of initial rolls
        if not token[3][1]:
            pass  # TODO: Throw error
        else:
            for r in _initialRolls:
                if token[3][0] == ">" and r > token[3][1]:
                    processedRolls.append(random.randint(1, token[1]))
                elif r < token[3][1]:
                    processedRolls.append(random.randint(1, token[1]))
                else:
                    processedRolls.append(r)

    elif token[2] == "ra":
        # TODO: Rewrite
        pass
        """
        _isDirty = True
        _initialRolls = initialRolls.copy()  # Preserve order of initial rolls
        if not token[3][1]:
            pass  # TODO: Throw error
        else:
            while _isDirty:
                _isDirty = False
                for idx, r in enumerate(_initialRolls):
                    if (token[3][0] == ">" and r > token[3][1]) or (r < token[3][1]):
                        _isDirty = True
                        _roll = random.randint(1, token[1])
                        processedRolls.append(_roll)
                        _initialRolls[idx] = _roll
                    else:
                        processedRolls.append(r)
                # TODO: Could be more efficient if we don't loop over all values every time one doesn't match.
        """
    elif token[2] == "!":
        # TODO: Exploding/Penetrating Dice
        pass

    else:
        processedRolls = initialRolls

    return RollPayload(
        invokingCommand=token,
        initialRolls=tuple(initialRolls),
        processedRolls=tuple(processedRolls)
    )


def displayRolls(rolls: RollPayload) -> str:
    """
    Builds string with Markdown formatting for discord.

    :param rolls: RollPayload object.
    :returns: (str): string representation of query + results to be printed.
    """
    # Roll Query
    _query = [f"{str(rolls.invokingCommand[0])}d{str(rolls.invokingCommand[1])}"]
    if rolls.invokingCommand[2]:
        _query.append(str(rolls.invokingCommand[2]))
    if rolls.invokingCommand[3][0]:
        _query.append(str(rolls.invokingCommand[3][0]))
    if rolls.invokingCommand[3][1]:
        if rolls.invokingCommand[3][1] != 0:
            _query.append(str(rolls.invokingCommand[3][1]))
    if rolls.invokingCommand[4]:
        if rolls.invokingCommand[4] != 0:
            _query.append(f"+{str(rolls.invokingCommand[4])}")
    _query.append("\n")

    # Roll Result
    out = ["("]
    if rolls.invokingCommand[2] in ['kh', 'kl']:
        _processedRolls = list(rolls.processedRolls)
        for idx, x in enumerate(rolls.initialRolls):
            if x in _processedRolls:
                out.append(f"{str(x)}")
                _processedRolls.remove(x)
            else:
                out.append(f"~~{str(x)}~~")

            if idx != len(rolls.initialRolls) - 1:
                out.append(", ")
        out.append(") ")

    elif rolls.invokingCommand[2] in ['ro']:
        for idx, (initialValue, processedValue) in enumerate(zip(rolls.initialRolls, rolls.processedRolls)):
            if initialValue == processedValue:
                out.append(f"{str(processedValue)}")
            else:
                out.append(f"~~{str(initialValue)}~~ -> {str(processedValue)}")

            if idx != len(rolls.initialRolls) - 1:
                out.append(", ")
        out.append(") ")

    else:
        for idx, x in enumerate(rolls.processedRolls):
            out.append(str(x))
            if idx != len(rolls.processedRolls) - 1:
                out.append(", ")
        out.append(") ")

    if rolls.invokingCommand[4] != 0:
        out.append(f"+ {str(rolls.invokingCommand[4])} = {str(sum(rolls.processedRolls) + rolls.invokingCommand[4])}")
    else:
        out.append(f"= {str(sum(rolls.processedRolls))}")
    return "".join(_query) + "".join(out)

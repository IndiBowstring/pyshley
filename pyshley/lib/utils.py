import typing


def clampIfExists(val: typing.Union[str, int, None], mini: int, maxi: int, default=0) -> int:
    return max(min(int(val), maxi), mini) if val else default

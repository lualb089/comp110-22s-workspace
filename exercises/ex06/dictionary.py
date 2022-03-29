"""Build some dictionary functions."""

__author__ = "730480432"


def invert(a: dict[str, str]) -> dict[str, str]:
    """The keys of the input list becomes the values of the output list and vice versa."""
    empty: dict[str, str] = {}
    for key in a:
        if a[key] in empty:
            raise KeyError
        empty[a[key]] = key
    return empty 


def favorite_color(a: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    frequently: dict[str, int] = {}
    color: str = ""
    for key in a:
        if a[key] in frequently:
            frequently[a[key]] += 1
        else:
            frequently[a[key]] = 1
    most: int = 0
    for key in frequently:
        if most < frequently[key]:
            most = frequently[key]
            color = key
    return color


def count(a: list[str]) -> dict[str, int]:
    """A dictionary of the counts of each of the items in the input list."""
    given: dict[str, int] = {}
    for value in a:
        if value in given:
            given[value] += 1
        else:
            given[value] = 1
    return given
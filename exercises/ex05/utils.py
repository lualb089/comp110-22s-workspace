"""Build some list utility functions."""

__author__ = "730480432"


def only_evens(xs: list[int]) -> list[int]:
    """A list containing only the elements of the input list that were even."""
    evens: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """A List which is a subset of the given list."""
    subset: list[int] = []
    while start < end:
        subset.append(xs[start])
        start += 1
    return subset


def concat(xs: list[int], past: list[int]) -> list[int]:
    """A list containing all elements of the first list, followed by all elements of the second list."""
    other: list[int] = []
    only_evens.extend(sub)
    return other
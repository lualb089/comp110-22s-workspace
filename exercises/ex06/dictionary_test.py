"""Test some dictionary functions."""

__author__ = "730480432"

import pytest

from dictionary import invert, favorite_color


def test_invert() -> None:
    """Testing the invert funct."""
    values = {'a': 'z', 'b': 'y', 'c': 'x'}
    invert(values)
    with pytest.raises(KeyError):
        new_val = {'kris': 'jordan', 'michael': 'jordan'}
        invert(new_val)


def test_favorite_color() -> None:
    """Testing the fav color funct."""
    values = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    favorite_color(values)
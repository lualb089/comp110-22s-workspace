"""Testing some list utility functions."""

__author__ = "730480432"

from utils import only_evens, sub 
# , concat


def test_only_evens_positive() -> None:
    """Testing to find only positive even numbers."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]


def test_only_evens_empty() -> None:
    """Testing to find only even numbers when given none.""" 
    assert only_evens([]) == []


def test_only_evens_negative() -> None:
    """Testing to find only negative even numbers."""
    assert only_evens([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-2, -4, -6, -8, -10]


def test_sub_positive() -> None:
    """Testing to find a subset in postive numbers"""

    assert sub([1, 2, 3, 4], 1, 3) == [2, 3] 


def test_sub_empty() -> None:
    """Testing to find a subset in postive numbers"""
    assert sub([], 1, 2) == []


def test_sub_negative() -> None:
    """Testing to find a subset in postive numbers"""
    assert sub([-1, -2, -3, -4], 1, 3) == [-2, -3]
"""Testing some list utility functions."""

__author__ = "730480432"

from utils import only_evens, sub, concat


def test_only_evens_positive() -> None:
    """Testing to find only positive even numbers."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]


def test_only_evens_empty() -> None:
    """Testing to find only even numbers when given none.""" 
    assert only_evens([]) == []


def test_only_evens_negative() -> None:
    """Testing to find only negative even numbers."""
    assert only_evens([0, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-2, -4, -6, -8, -10]


def test_sub_positive() -> None:
    """Testing to find a subset in postive numbers."""
    a_list = [1, 2, 3, 4, 5]
    assert sub(a_list, 1, 3) == [2, 3] 


def test_sub_empty() -> None:
    """Testing to find a subset in no numbers."""
    a_list = []
    assert sub(a_list, 1, 2) == []


def test_sub_negative() -> None:
    """Testing to find a subset in negative numbers."""
    a_list = [-1, -2, -3, -4, -5]
    assert sub(a_list, 1, 3) == [-2, -3]


def test_concat_positive() -> None:
    """Testing to find list in postive numbers."""
    assert concat


def test_concat_empty() -> None:
    """Testing to find list in no numbers."""
    assert concat


def test_concat_negative() -> None:
    """Testing to find list in negative numbers."""
    assert concat
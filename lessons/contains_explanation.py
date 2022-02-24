"""Example of a function that searches through a list."""

# Define a function named contains
# Two parameters:
#   1. needle - the string we're searching for
#   2. haystack - the list we're searching through


def contains(needle: str, haystack: list[str]) -> bool:

    # Algorithm:
    #   For each item in the haystack
    #       Test if it equal to the needle
    #           If so, return True
    for item in haystack:
        if item == needle:
            return True
    
# After testing all items, return False, because not found
# Returns True if needle in haystack, False otherwise
    return False

"""Some examples of tender, loving."""

name = input("What's your name? ")

a: str = str(print(f"I love you {name}! "))


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"



def spread_love(to: str, n:int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    count: int = 0
    while count < n:
        count = count + 1
        love_note = love_note + love(to) + "/n"
    return love_note

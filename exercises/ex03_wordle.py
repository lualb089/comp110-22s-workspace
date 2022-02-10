"""Ex03 - Wordle."""

__author__ = "730480432"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    codes: str = "car"
    first: str = ""
    i: int = 1
    exp_length: int = len(codes)

    while i < 7:
        print(f"=== Turn {i}/6 ===")
        first = (input_guess(exp_length))
        print(emojified(first, codes))
        if first == codes:
            print(f"You won in {i}/6 turns!")
            i = 10
        i = i + 1
    if first != codes:
        print("x/6 - Sorry, try again tomorrow!")


def contains_char(search: str, single: str) -> bool:
    """Figures out if a character is in a word."""
    assert len(single) == 1
    i: int = 0
    while i < len(search):
        if search[i] == single:
            return True
        i = i + 1  
    return False


def emojified(guess: str, secret: str) -> str:
    """Finds if guess is in the secret."""
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0
    
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji


def input_guess(exp_length: int) -> str:
    """Ensures user uses the correct length."""
    word: str = input(f"Enter a {exp_length} character word: ")

    while len(word) != exp_length:
        word = input(f"That wasn't {exp_length} chars! Try again: ")
    return word


if __name__ == "__main__":
    main()
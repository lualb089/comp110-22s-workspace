"""Ex02 - Wordle: One-shot."""

__author__ = "730480432"

secret = "python"

guess: str = input(f"What is your { len(secret) }-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not { len(secret) } letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0

emoji: str = ""

while index < len(secret):
    if guess[index] == secret[index]:
        emoji = emoji + GREEN_BOX
    else:
        other_ch: bool = False
        match: int = 0
        while not other_ch and match < len(secret):
            if guess[index] == secret[match]:
                other_ch = True
            match = match + 1
        if other_ch:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1
print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon! ")
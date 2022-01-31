"""An example of (what-if) statements"""

SECRET: int = 3

print("I am thinking of a number between 1 and 5. ")
guess: int = int(input("What is ur guess? "))

if guess == SECRET:
    print("You guessed correctly!!! ")
    print("Have a nice day! ")
else:
    print("Sorry, you guessed incorrectly :( ") 
    if guess > SECRET:
        print("You guessed too high ")
    else:
        print("You guessed too low ")

print("Game Over. ")
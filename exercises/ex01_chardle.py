"""Ex01 - Charadle - A cute step toward Wordle."""

__author__ = "730480432"

five_ch: str = input("Enter a 5-character word: ")

if len(five_ch) != 5:
    print("Error: Word must contain 5 characters ")
    exit()

single_ch: str = input("Enter a single character: ")

if len(single_ch) != 1:
    print("Error: Character must be a single character. ")
    exit()

print("Searching for " + single_ch + " in " + five_ch)

count_ch: int = 0

if five_ch[0] == single_ch:
    print(single_ch + " found at index 0")
    count_ch = count_ch + 1

if five_ch[1] == single_ch:
    print(single_ch + " found at index 1")
    count_ch = count_ch + 1 

if five_ch[2] == single_ch:
    print(single_ch + " found at index 2")
    count_ch = count_ch + 1

if five_ch[3] == single_ch:
    print(single_ch + " found at index 3")
    count_ch = count_ch + 1

if five_ch[4] == single_ch:
    print(single_ch + " found at index 4")
    count_ch = count_ch + 1

if count_ch == 0:
    print("No instances of " + single_ch + " found in " + five_ch)
else:
    if count_ch == 1:
        print(str(count_ch) + " instance of " + single_ch + " found in " + five_ch)
    if count_ch > 1:
        print(str(count_ch) + " instances of " + single_ch + " found in " + five_ch)
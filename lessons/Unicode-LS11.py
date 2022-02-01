"""Looking at individual characters and asking what a character really is."""

ord("A")
ord("B")

ord("a")
ord("b")


chr(65)
chr(122)
chr(ord('A'))
ord(chr(65))

print("The \U0001F920 rides a \U0001F40E!")
print("110 is on a \U0001F6A2")
print("I really love to \U0001F973")

emoji: str = "\U0001F920\U0001F40E"
print(emoji)
print(len(emoji))
print(emoji[0])

print("Hello\nworld\n!!!")

print("The computer said, \"Hello, world.\"")
print("The computer said, Hello, world.")

course: int = 110
print("I am in COMP" + str(course) + " right now!")
print(f"I am in COMP{ course } right now!")

name: str = "Lauren"
age_turning: int = 21
print("Hello " + name + ", you're almost " + str(age_turning) + "!")
print(f"Hello {name}, you're almost {age_turning}!")

age: int = 21
msg: str = f"You are {age}!"
print(msg)
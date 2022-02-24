"""Prep for EX04"""


from turtle import Turtle, colormode, done
leo: Turtle = Turtle()


side_length: int = 300

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
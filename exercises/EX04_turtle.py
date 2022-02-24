"""A sun with two happy trees."""

__author__ = "730480432"

from turtle import Turtle, colormode, done 


def main() -> None:
    """The entrypoint of my scene."""
    sun: Turtle = Turtle()
    sun.hideturtle()
    circle(sun, -200, 100)
    tree_trunk(sun, 50, -50)
    tree(sun, 110, -10)
    tree_trunk(sun, 200, -50)
    tree(sun, 260, -10)
    star(sun, 200, 233)
    star(sun, 150, 190)
    star(sun, 90, 200)
    star(sun, 270, 250)
    star(sun, 25, 245)
    star(sun, 220, 110)
    star(sun, 99, 80)
    star(sun, 10, 112)
    star(sun, -90, 233)
    star(sun, -75, 110)
    star(sun, 50, 160)
    star(sun, 20, 180)
    star(sun, -20, 190)
    done()


def circle(sun: Turtle, x: float, y: float) -> None:
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    colormode(255)
    sun.color("#f5c71a")
    sun.begin_fill()
    sun.circle(100)
    sun.end_fill()


def tree_trunk(sun: Turtle, x: float, y: float) -> None:
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.color("#654321")
    sun.begin_fill()
    sun.forward(20)    
    sun.left(90)
    sun.forward(40)
    sun.left(90)
    sun.forward(20)
    sun.left(90)
    sun.forward(40)
    sun.end_fill()


def tree(sun: Turtle, x: float, y: float) -> None:
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.color("#006400")
    sun.begin_fill()
    sun.right(150)
    sun.forward(100)
    sun.left(120)
    sun.forward(100)
    sun.left(120)
    sun.forward(100)
    sun.end_fill()


def star(sun: Turtle, x: float, y: float) -> None:
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.color("#FFC0CB")
    sun.begin_fill()

    for i in range(5):
        sun.forward(30)
        sun.right(144)
    sun.end_fill()


if __name__ == "__main__":
    main()

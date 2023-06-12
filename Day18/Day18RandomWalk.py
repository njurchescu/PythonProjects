import random
from random import randrange, randint
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.colormode(255)
tim.speed("fast")

thickness = 0


def direction():
    return random.choice([0, 90, 180, 270])


for _ in range(100):
    # thickness += 0.01
    rgb = (randrange(255), randrange(255), randrange(255))
    tim.color(rgb)
    tim.pensize(10)
    tim.setheading(direction())
    tim.forward(20)

screen.exitonclick()

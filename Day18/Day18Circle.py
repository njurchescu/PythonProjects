import random
from random import randrange, randint
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.colormode(255)
tim.speed("fastest")


heading = 0

for _ in range(int(360/5)):
    rgb = (randrange(255), randrange(255), randrange(255))
    tim.color(rgb)
    tim.circle(50)
    tim.setheading(tim.heading() + 5)


screen.exitonclick()
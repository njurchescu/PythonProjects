
from random import randrange
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.colormode(255)

side = 3
angle = 360
while angle > 36:

    angle = 360 / side
    rgb = (randrange(255), randrange(255), randrange(255))
    for _ in range(side):
        tim.pencolor(rgb)
        tim.right(angle)
        tim.forward(100)
    side += 1

'''    Different solution
def draw_shape(sides,side_color):
    angle = 360 / sides
    for _ in range(sides):
        tim.pencolor(side_color)
        tim.right(angle)
        tim.forward(100)


side = 3
for shape_side_n in range(3, 11):
    rgb = (randrange(255), randrange(255), randrange(255))
    draw_shape(side, rgb)
    side += 1

'''



#
#







screen.exitonclick()
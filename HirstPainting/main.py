# import colorgram

# color_list = colorgram.extract('hirst.jpg', 8)
# # print(colors)
# colors = []
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     colors.append(new_color)
# print(colors)

import random
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.goto(-200,-230)
our_colors = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5)]

new_y_position = tim.ycor()
x_cor = tim.xcor()
for i in range(10):
    new_y_position += 50
    for _ in range(10):
        tim.dot(20, random.choice(our_colors))
        tim.forward(50)
    tim.goto(x_cor, new_y_position)


screen.exitonclick()
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

y_cor = -100
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_cor)
    all_turtles.append(new_turtle)

    y_cor += 40


is_game_on = False

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
               print(f"You've won, winning turtle is {winning_turtle}.")
            else:
                print(f"You've lost, winning turtle is {winning_turtle}.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()

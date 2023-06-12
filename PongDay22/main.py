from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


def check_score(right, left):
    if right == 2:
        return "right"
    if left == 2:
        return "left"


game_on = True

while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #     Detect paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #     Detect off limit wall/r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.check_winner():
        game_on = False



screen.exitonclick()

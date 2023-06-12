from turtle import Turtle, Screen

tim = Turtle()
tim_2 = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim_2.backward(10)


def move_counter():
    tim.right(10)


def move_clockwise():
    tim.left(10)


def clear_screen():
    tim.home()
    tim.clear()



screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counter)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

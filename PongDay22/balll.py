from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("purple")
        # self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.setheading(40)

    def move(self):
        self.forward(10)



    def change_direction(self):
        new_heading = self.heading()
        self.setheading(new_heading + 180)


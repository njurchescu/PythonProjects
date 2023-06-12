from turtle import Turtle

FONT = ("Courier", 14, "normal")
POSITION = (-230, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="Center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_finished(self):
        self.home()
        self.write("GAME OVER", align="Center", font=("Courier", 30, "normal"))


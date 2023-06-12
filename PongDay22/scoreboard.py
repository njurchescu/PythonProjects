from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 11, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def check_winner(self):
        if self.r_score == 2:
            self.home()
            self.write(f"Right player won.", align=ALIGNMENT, font=("Courier", 40, "normal"))
            return True
        if self.l_score == 2:
            self.home()
            self.write(f"Left player won.", align=ALIGNMENT, font=("Courier", 40, "normal"))
            return True


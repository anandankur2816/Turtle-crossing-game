from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.wr()

    def wr(self):
        self.goto(-225, 265)
        self.write(f"Level:{self.score}", align='center', font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.wr()


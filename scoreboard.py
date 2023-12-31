from turtle import Turtle

FONT = ("Lucida Console", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write_score()

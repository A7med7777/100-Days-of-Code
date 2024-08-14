from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.pen(shown=False, pendown=False)
        self.setpos(-260, 260)
        self.write_score()

    def write_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", move=False, align="center", font=FONT)

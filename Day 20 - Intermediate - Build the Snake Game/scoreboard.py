from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.pen(pendown=False, pencolor="white")
        self.setpos(-300, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=("courier", 20, "normal"))

from turtle import Turtle


def get_high_score():
    try:
        with open("high.txt", "r") as file:
            num = file.read()
            int_num = int(num)
            return int_num
    except FileNotFoundError:
        return 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = get_high_score()
        self.hideturtle()
        self.pen(pendown=False, pencolor="white")
        self.setpos(-300, y=240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()

        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align='left',
            font=('Courier', 20, 'normal')
        )

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align='center', font=("courier", 20, "normal"))
        if self.score > self.high_score:
            with open("high.txt", "w") as file:
                score = str(self.score)
                file.write(score)

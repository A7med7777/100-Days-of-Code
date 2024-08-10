from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.right = 0
        self.left = 0
        self.pen(shown=False, pendown=False, fillcolor="white", pencolor="white")
        self.setpos(0, 234)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.left} | {self.right}", move=False, align='center', font=('Courier', 75, 'normal'))

    def increment_right(self):
        self.right += 1
        self.write_score()

    def increment_left(self):
        self.left += 1
        self.write_score()


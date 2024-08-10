from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.num_x = 1
        self.num_y = 1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        x = self.xcor() + self.num_x
        y = self.ycor() + self.num_y
        self.setpos(x, y)

    def reset_pos(self):
        self.setpos(0, 0)

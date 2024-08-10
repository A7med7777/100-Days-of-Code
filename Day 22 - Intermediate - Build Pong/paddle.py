from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setpos(self.position)

    def move_up(self):
        if self.ycor() < 300:
            self.setpos(self.xcor(), self.ycor() + 12)

    def move_down(self):
        if self.ycor() > -300:
            self.setpos(self.xcor(), self.ycor() - 12)

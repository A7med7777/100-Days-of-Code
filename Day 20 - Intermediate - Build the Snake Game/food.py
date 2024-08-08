import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pen(pendown=False, pencolor="green", fillcolor="green")
        self.shapesize(0.8)
        self.random_location()

    def random_location(self):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        self.setpos(x, y)

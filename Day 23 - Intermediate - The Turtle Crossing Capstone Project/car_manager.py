from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for color in COLORS:
            if not randint(0, 5):
                car = Turtle("square")
                car.shapesize(1, 2)
                car.penup()
                car.color(color)
                car.setpos(300, randint(-250, 250))
                self.cars.append(car)

    def move_cars(self):
        for index, car in enumerate(self.cars):
            if car.xcor() < -321:
                self.cars.pop(index)

            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    for car in car_manager.cars:
        if player.distance(car) <= 23:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.write_score()
        player.setpos(0, -280)
        car_manager.increase_speed()

    if not random.randint(0, 5):
        car_manager.generate_cars()

    car_manager.move_cars()
    
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

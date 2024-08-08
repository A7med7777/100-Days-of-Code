from snake import Snake
from turtle import Screen
import time

screen = Screen()
snake = Snake()

screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.face_north, key="Up")
screen.onkey(fun=snake.face_west, key="Left")
screen.onkey(fun=snake.face_south, key="Down")
screen.onkey(fun=snake.face_east, key="Right")

while True:
    snake.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()

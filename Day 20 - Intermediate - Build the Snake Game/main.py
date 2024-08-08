from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(fun=snake.face_north, key="Up")
screen.onkey(fun=snake.face_west, key="Left")
screen.onkey(fun=snake.face_south, key="Down")
screen.onkey(fun=snake.face_east, key="Right")

game_over = False

while not game_over:
    snake.move()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 15:
            game_over = True
            scoreboard.game_over()

    if snake.head.xcor() > 300 or snake.head.xcor() < -310 or snake.head.ycor() > 260 or snake.head.ycor() < -250:
        game_over = True
        scoreboard.game_over()

    if food.distance(snake.head) < 15:
        scoreboard.update_scoreboard()
        food.random_location()
        snake.grow()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import Board
import time

screen = Screen()
screen.title("Pong")
screen.tracer(0)
screen.setup(987, 654)
screen.bgcolor("black")
screen.listen()

ball = Ball()
board = Board()

paddle_right = Paddle((472, 0))
paddle_left = Paddle((-480, 0))
paddle_right.create_paddle()
paddle_left.create_paddle()

screen.onkeypress(fun=paddle_right.move_up, key="Up")
screen.onkeypress(fun=paddle_left.move_up, key="w")
screen.onkeypress(fun=paddle_right.move_down, key="Down")
screen.onkeypress(fun=paddle_left.move_down, key="s")

game_over = False
delay = 0.01

while not game_over:
    if ball.ycor() > 315 or ball.ycor() < -310:
        ball.num_y *= -1

    if ball.xcor() > 474:
        board.increment_left()
        ball.reset_pos()
        delay = 0.01

    if ball.xcor() < -484:
        board.increment_right()
        ball.reset_pos()
        delay = 0.01

    if ball.xcor() >= 456 and paddle_right.distance(ball) <= 43:
        delay -= 0.0011
        ball.num_x *= -1

    if ball.xcor() <= -456 and paddle_left.distance(ball) <= 43:
        delay -= 0.0011
        ball.num_x *= -1

    ball.move()
    time.sleep(delay if delay >= 0 else 0.0011)
    screen.update()

screen.exitonclick()

from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []

screen = Screen()


def create_turtles(color_list):
    y = -200

    for color in color_list:
        tim = Turtle(shape="turtle")
        tim.color(color)
        y += 50
        tim.setpos(-300, y)
        turtles.append(tim)


user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color:\n(red, orange, yellow, green, blue, indigo, violet)"
)

create_turtles(colors)
finish = False

while not finish:
    for turtle in turtles:
        if turtle.xcor() < 290:
            turtle.forward(random.randint(0, 10))
        else:
            finish = True
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            break

screen.exitonclick()

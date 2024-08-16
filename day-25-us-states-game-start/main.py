from turtle import Turtle, Screen
import pandas

screen = Screen()
tim = Turtle()

tim.penup()

screen.setup(735, 500)
screen.bgpic("./blank_states_img.gif")

states_data = pandas.read_csv("./50_states.csv")
states_list = states_data.to_dict("records")

while states_list:
    answer = screen.textinput(
        title=f"{50 - len(states_list)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()

    if answer == "Quit":
        break

    for index, state in enumerate(states_list):
        state_name = state["state"]

        if state_name == answer:
            x = state["x"]
            y = state["y"]
            tim.goto(x, y)
            tim.write(state_name, move=False, align='left', font=('Arial', 8, 'normal'))
            states_list.pop(index)
            break

data = pandas.DataFrame(states_list)
data.to_csv("states_to_learn.csv")
print(data)

screen.exitonclick()

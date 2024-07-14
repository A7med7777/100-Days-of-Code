def turn_right():
    for n in range(3):
        turn_left()


def jump():
    turn_left()

    while not right_is_clear():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

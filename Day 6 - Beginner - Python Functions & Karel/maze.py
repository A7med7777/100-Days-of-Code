def turn_right():
    for n in range(3):
        turn_left()


while not at_goal():
    if not right_is_clear() and front_is_clear():
        move()
    elif not right_is_clear() and not front_is_clear():
        turn_left()
    elif right_is_clear() and not front_is_clear():
        turn_right()
        move()
    elif front_is_clear and right_is_clear():
        while not is_facing_north():
            turn_left()

        while front_is_clear():
            move()

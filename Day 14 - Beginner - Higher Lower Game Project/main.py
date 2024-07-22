from game_data import data
from art import logo, vs
from random import choice
import os

score = 0
answer = True
game_on = True
local_data = data.copy()
a = choice(local_data)

while game_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    if answer:
        local_data.pop(local_data.index(a))
        b = choice(local_data)

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        while user_choice not in ["a", "b"]:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice == "a" and a["follower_count"] < b["follower_count"]:
            answer = False
        elif user_choice == "b" and a["follower_count"] > b["follower_count"]:
            answer = False
        else:
            a = b
            score += 1

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False

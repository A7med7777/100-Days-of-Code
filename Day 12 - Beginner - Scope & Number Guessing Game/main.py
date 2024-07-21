from art import logo
from random import randint

attempts = 10
end_of_game = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty not in ["easy", "hard"]:
    difficulty = input("Invalid choice. Please type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    attempts = 5

num = randint(1, 100)

while not end_of_game:
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break

    print(f"You have {attempts} attempts remaining to guess the number.")

    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        if guess == num:
            print(f"You got it! The answer was {num}.")
            end_of_game = True
        elif guess > num:
            print("Too high.")
            attempts -= 1
        elif guess < num:
            print("Too low.")
            attempts -= 1

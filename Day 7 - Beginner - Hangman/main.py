from hangman_art import logo, stages
from hangman_words import word_list
import random
import os

random_word = random.choice(word_list)
lives = 7
end_of_game = False
guessed = ["_" for _ in range(len(random_word))]
guessed_letters = set()

print(logo)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear_screen()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.add(guess)
        if guess in random_word:
            for idx, letter in enumerate(random_word):
                if letter == guess:
                    guessed[idx] = guess

            if "_" not in guessed:
                print("You win.")
                end_of_game = True
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

            if lives == 0:
                print("You lose.")
                end_of_game = True

    print("".join(guessed))

    if lives != 7:
        print(stages[lives])

print(f"The word was: {random_word}")

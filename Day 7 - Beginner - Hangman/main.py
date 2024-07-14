from hangman_art import logo, stages
from hangman_words import word_list
import random
import os

random_word = random.choice(word_list)
lives = 7
end_of_game = False
guessed = ["_" for _ in range(len(random_word))]
print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    if guess in guessed:
        print(f"You've already guessed {guess}")
    elif guess in random_word:
        guessed[random_word.index(guess)] = guess

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

print(random_word)

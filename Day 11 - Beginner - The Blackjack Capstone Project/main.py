from art import logo, deck
from random import randint, choice
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw():
    return choice(cards)


def check_blackjack(hand):
    return sum(hand) == 21 and len(hand) == 2


play = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while play:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_again == "n":
        play = False
    else:
        clear_screen()
        print(logo)
        hit = True
        user = [draw()]
        computer = [draw(), draw()]

        while hit:
            user.append(draw())
            user_score = sum(user)
            computer_score = sum(computer)
            print("Your cards:", end="")

            for card in user:
                print(deck[card][randint(0, 15) if card == 10 else randint(0, 3)], end="")

            print(f"current score: {user_score}")

            print(f"Computer's first card:"
                  f"{deck[computer[0]][randint(0, 15) if computer[0] == 10 else randint(0, 3)]}")

            if check_blackjack(user):
                print("Win, You have Blackjack 🃏")
                hit = False
            elif check_blackjack(computer):
                print("Lose, opponent has Blackjack 😱")
                hit = False
            else:
                if user_score > 21 and 11 in user:
                    user[user.index(11)] = 1
                    user_score = sum(user)
                if user_score > 21:
                    print("You went over. You lose 😭")
                    hit = False
                else:
                    more_cards = input("Type 'y' to hit(take more cards), type 'n' to stand(keep current hand): ")

                    if more_cards == "n":
                        hit = False

                        while computer_score < 17:
                            computer.append(draw())
                            computer_score = sum(computer)

                        print(f"Computer's final hand: {computer}, final score: {computer_score}")

                        if computer_score > 21:
                            print("Opponent went over. You win 😁")
                        else:
                            if user_score == computer_score:
                                print("Draw 🙃")
                            elif user_score > computer_score:
                                print("You win 😃")
                            elif computer_score > user_score:
                                print("You lose 😤")

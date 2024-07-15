from art import logo
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


bidders = {}
max_bid = 0
winner = ""

while True:
    print(logo)
    name = input("What is your name?: ").title()

    try:
        bid = float(input("What is your bid?: $"))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the bid.")
    else:
        bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    while other_bidders not in ["yes", "no"]:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidders == "no":
        break
    elif other_bidders == "yes":
        clear_screen()

for bidder in bidders:
    if bidders[bidder] > max_bid:
        max_bid = bidders[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${bidders[winner]}\n", bidders)

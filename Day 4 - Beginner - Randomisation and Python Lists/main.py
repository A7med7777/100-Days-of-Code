import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

while True:
    try:
        prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    except ValueError as ve:
        print(ve)
    else:
        if prompt > 2 or prompt < 0:
            print()
        else:
            computer = random.randint(0, 2)
            print(choice[prompt])
            print("Computer chose: ")
            print(choice[computer])
            if prompt == computer:
                print("It's a draw")
            elif prompt == 0 and computer == 2:
                print("You win!")
            elif computer == 0 and prompt == 2:
                print("You lose")
            elif prompt > computer:
                print("You win!")
            else:
                print("You lose")
            break

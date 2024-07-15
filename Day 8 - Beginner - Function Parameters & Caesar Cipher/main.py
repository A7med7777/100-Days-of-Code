from art import logo


def cipher(message_txt, shift_num, action):
    coded_msg = ""
    shifting = shift_num % 26

    for letter in message_txt:
        if letter not in alphabet:
            coded_msg += letter
        else:
            coded_msg += alphabet[
                alphabet.index(letter) + shifting if action == "encode" else alphabet.index(letter) - shifting
            ]

    return coded_msg


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_again = True

while go_again:
    print(logo)
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if choice in ["encode", "decode"]:
        message = input("Type your message:\n").lower()

        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Invalid shift number. Please enter an integer.")
        else:
            print(f"Here's the {choice}d result: " + cipher(message, shift, choice))
    else:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue

    again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    while again != "yes" and again != "no":
        again = input("Invalid input. Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if again == "no":
        print("Goodbye")
        go_again = False

print("Welcome to the Band Name Generator.")

while True:
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")

    if city and pet:
        print(f"Your band name could be '{city} {pet}'".title())
        break
    else:
        print("These fields are required! Try again.\n")

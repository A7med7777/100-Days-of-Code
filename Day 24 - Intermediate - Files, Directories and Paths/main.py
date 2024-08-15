with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
    
strip_names = [name.strip("\n") for name in names]

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

for name in strip_names:
    with open(f"./Output/ReadyToSend/{name}.txt", "w", encoding="utf-8") as file:
        new_letter = letter.replace("[name]", name)
        file.write(new_letter)

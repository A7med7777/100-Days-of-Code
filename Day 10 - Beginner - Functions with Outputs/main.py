from art import logo
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(first_number, next_number):
    return first_number + next_number


def sub(first_number, next_number):
    return first_number - next_number


def mul(first_number, next_number):
    return first_number * next_number


def div(first_number, next_number):
    if next_number == 0:
        return "Error! Division by zero."
    return first_number / next_number


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

while True:
    clear_screen()
    continue_op = True
    print(logo)

    try:
        first_num = float(input("What's the first number?: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    while continue_op:
        op = input("+\n-\n*\n/\nPick an operation: ")

        if op not in operations:
            print("Invalid operation. Please pick a valid operation.")
            continue

        try:
            next_num = float(input("What's the next number?: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        result = operations[op](first_num, next_num)
        print(f"{first_num} {op} {next_num} = {result}")

        if isinstance(result, str):  # Check if there's an error message
            continue_op = False
            continue

        first_num = result
        continue_with = input(f"Type 'y' to continue calculating with {first_num}, "
                              f"or type 'n' to start a new calculation: ").lower()

        if continue_with == "n":
            continue_op = False

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def resources_sufficient(user_choice):
    sufficient = True

    for resource in MENU[user_choice]["ingredients"]:
        if resources[resource] < MENU[user_choice]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            sufficient = False

    return sufficient


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(user_choice):
    coins = process_coins()
    cost = MENU[user_choice]["cost"]

    if coins < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = coins - cost
        print(f"Here is ${change:.2f} in change.")
        resources["money"] += cost
        return True


def make_coffee(user_choice):
    ingredients = MENU[user_choice]["ingredients"]

    for ingredient, ingredient_cost in ingredients.items():
        resources[ingredient] -= ingredient_cost

    print(f"Here is your {user_choice}☕. Enjoy!")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },

        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },

        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },

        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

system_on = True

while system_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        system_on = False
    elif prompt == "report":
        print_report()
    elif prompt in MENU.keys():
        try:
            if resources_sufficient(prompt):
                if transaction_successful(prompt):
                    make_coffee(prompt)
        except ValueError as ve:
            print(ve)

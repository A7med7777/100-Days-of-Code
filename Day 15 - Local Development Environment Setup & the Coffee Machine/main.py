from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

system_on = True

while system_on:
    prompt = input(f"What would you like? ({menu.get_items()}): ")

    if prompt == "off":
        system_on = False
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(prompt)

        if menu_item and coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)

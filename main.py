# Ruben Sanduleac
# Date: January 27th, 2022
# Description: This program has been redone for OOP. It simulates a coffee machine where the user
#              places a specific amount and selects a drink. If the amount is
#              over the needed amount the sum is refunded.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from background import logo

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
# while loop for the program
while is_on:
    print(logo)
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

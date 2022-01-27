# Ruben Sanduleac
# Date: January 26th, 2022
# Description: This program simulates a coffee machine where the user
#              places a specific amount and selects a drink. If the amount is
#              over the needed amount the sum is refunded.
# DONE: Prompt user by asking "What would you like? (espresso/latte/cappuccino):”

from menu_coffee import resources
from res import MENU

# Global Variable for coin values
QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01
# Global Variable for keeping track of the profit by the machine
MONEY = 0.00
# Bool to continue running the machine until the user types 'off'
OFF = False


def enough_money(q, d, n, p):
    """This function returns the total amount of money based on the coins that were inputed."""
    # Counter that keeps track of the total amount the user entered
    total = 0
    # calculations for the total
    total += ((q * QUARTERS) + (d * DIMES) + (n * NICKELS) + (p * PENNIES))
    # return the total back to the main
    return total


def resources_pass(drinks, sums):
    """This function receives two inputs 'drinks' responsible for checking if the possible
    drink is in the menu. In addition, the function returns the change back. The sums input is also
    responsible for taking in the amount and calculating the difference between the two"""
    # compare the input from the user for the drinks with the menu
    if drinks == 'espresso':
        # if the cost in the menu is less than or equal to the amount the user entered.
        if MENU['espresso']['cost'] <= sums:
            # calculate the change
            coin_change = sums - (MENU['espresso']['cost'])
            # return the change back to the main.
            return coin_change
        else:
            # else return a flag int for not enough money
            return -1
    # compare the input from the user for the drinks with the menu
    elif drinks == 'latte':
        # if the cost in the menu is less than or equal to the amount the user entered.
        if MENU['latte']['cost'] <= sums:
            # calculate the change
            coin_change = sums - (MENU['latte']['cost'])
            # return the change back to the main.
            return coin_change
        else:
            # else return a flag int for not enough money
            return -1
    # compare the input from the user for the drinks with the menu
    elif drinks == 'cappuccino':
        # if the cost in the menu is less than or equal to the amount the user entered.
        if MENU['cappuccino']['cost'] <= sums:
            # calculate the change
            coin_change = sums - (MENU['cappuccino']['cost'])
            # return the change back to the main.
            return coin_change
        else:
            # else return a flag int for not enough money
            return -1
    else:
        # return a second flag that the possible input was not valid
        return -2


def enough_ingredient(drinks):
    """This function gets passed 'drinks' and it is used to check
    if there are enough ingredients left in the resources file. The drinks is compared then
    the amount is deducted from the resources in the res.py file which are stored in a dictionary"""
    # If the valid drink matches the one in the dictionary
    if drinks == 'espresso':
        # check if there is enough water, and coffee in the resources file less than or equal to
        if MENU['espresso']['ingredients']['water'] <= resources['water']:
            if MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
                # subtract the amount needed from the resources from the amount required in MENU
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                # return back to main that it is possible to create the drink
                return 'possible'
            else:
                # return the missing resource and let the user know
                return 'coffee'
        else:
            # return the missing resource and let the user know
            return 'water'
    elif drinks == 'latte':
        if MENU['latte']['ingredients']['water'] <= resources['water']:
            if MENU['latte']['ingredients']['milk'] <= resources['milk']:
                if MENU['latte']['ingredients']['coffee'] < resources['coffee']:
                    resources['water'] -= MENU['latte']['ingredients']['water']
                    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                    resources['milk'] -= MENU['latte']['ingredients']['milk']
                    return 'possible'
                else:
                    return 'coffee'
            else:
                return 'milk'
        else:
            return 'water'
    elif drinks == 'cappuccino':
        if MENU['cappuccino']['ingredients']['water'] <= resources['water']:
            if MENU['cappuccino']['ingredients']['milk'] <= resources['milk']:
                if MENU['cappuccino']['ingredients']['coffee'] <= resources['coffee']:
                    resources['water'] -= MENU['cappuccino']['ingredients']['water']
                    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                    return 'possible'
                else:
                    return 'coffee'
            else:
                return 'milk'
        else:
            return 'water'

    # elif drinks == 'report':
    #     print(f"Water: {resources['water']}")
    #     print(f"Coffee: {resources['coffee']}")
    #     print(f"Milk: {resources['milk']}")
    #     print(f"Money: ${MONEY}")
    # elif drinks == 'off':
    #     return True


# print(MENU['espresso']['cost'])

while not OFF:
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink == 'off':
        OFF = True
        break
    elif drink == 'report':
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"Money: ${MONEY:.2f}")
    is_possible = enough_ingredient(drink)
    if is_possible == 'possible':
        print("Please insert coins.")
        quarter_amount = int(input("How many quarters?: "))
        dimes_amount = int(input("How many dimes?: "))
        nickle_amount = int(input("How many nickles?: "))
        pennie_amount = int(input("How many pennies?: "))
        money_sum = enough_money(quarter_amount, dimes_amount, nickle_amount, pennie_amount)
        ready = resources_pass(drink, money_sum)
        if ready > 0:
            MONEY += MENU[drink]['cost']
            print(f"Here is your ${ready:.2f} in change.")
            print(f"Here is your {drink}. Enjoy!")
        elif ready >= -1:
            print("Not enough money. Money refunded. Please try again.")
        else:
            print("Invalid selection. Money refunded. Please try again.")
    elif is_possible == 'coffee' or is_possible == 'milk' or is_possible == 'water':
        print(f"Not enough {is_possible}")

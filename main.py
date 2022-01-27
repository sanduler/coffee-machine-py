# Ruben Sanduleac
# Date: January 26th, 2022
# Description: This program simulates a coffee machine where the user
#              places a specific amount and selects a drink. If the amount is
#              over the needed amount the sum is refunded.
# DONE: Prompt user by asking "What would you like? (espresso/latte/cappuccino):”

from menu_coffee import resources
from res import MENU

QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01
MONEY = 0.00
OFF = False


def enough_money(q, d, n, p):
    """This function returns the total amount of money based on the coins that were inputed."""
    total = 0
    total += ((q * QUARTERS) + (d * DIMES) + (n * NICKELS) + (p * PENNIES))
    return total


def resources_pass(drinks, sums):
    if drinks == 'espresso':
        if MENU['espresso']['cost'] <= sums:
            coin_change = sums - (MENU['espresso']['cost'])
            return coin_change
        else:
            return -1
    elif drinks == 'latte':
        if MENU['latte']['cost'] <= sums:
            coin_change = sums - (MENU['latte']['cost'])
            return coin_change
        else:
            return -1
    elif drinks == 'cappuccino':
        if MENU['cappuccino']['cost'] <= sums:
            coin_change = sums - (MENU['cappuccino']['cost'])
            return coin_change
        else:
            return -1
    else:
        return -2


def enough_ingredient(drinks):
    if drinks == 'espresso':
        if MENU['espresso']['ingredients']['water'] <= resources['water']:
            if MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                return 'possible'
            else:
                return 'coffee'
        else:
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
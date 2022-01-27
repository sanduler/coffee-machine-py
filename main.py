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
MONEY = 0


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
        if MENU['cappuccino']['ingredients']['water'] < resources['water']:
            if MENU['cappuccino']['ingredients']['coffee'] < resources['coffee']:
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                return 'possible'
            else:
                return 'coffee'
        else:
            return 'water'
    elif drinks == 'latte':
        if MENU['latte']['ingredients']['water'] < resources['water']:
            if MENU['latte']['ingredients']['milk'] < resources['milk']:
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
        if MENU['cappuccino']['ingredients']['water'] < resources['water']:
            if MENU['cappuccino']['ingredients']['milk'] < resources['milk']:
                if MENU['cappuccino']['ingredients']['coffee'] < resources['coffee']:
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

    elif drinks == 'report':
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"Money: ${MONEY}")


# print(MENU['espresso']['cost'])
drink = input("What would you like? (espresso/latte/cappuccino):").lower()
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

    elif ready >= -1:
        print("Not enough money. Money refunded. Please try again.")
    else:
        print("Invalid selection. Money refunded. Please try again.")
# else:
#     print(f"Sorry there is not enough {is_possible}")


# TODO: Check the user’s input to decide what to do next.
# TODO: Check if The prompt should show every time action has completed, e.g.
# once the drink is dispensed. The prompt should show again to serve the next customer.
# TODO: Turn off the Coffee Machine by entering “off” to the prompt.
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# TODO: Print report.
# When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# TODO: Check resources sufficient?
# When the user chooses a drink, the program should check if there are enough resources to make that drink.
# E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
# It should not continue to make the drink but print: “Sorry there is not enough water.”
# The same should happen if another resource is depleted, e.g. milk or coffee.
# TODO: Process coins.
# If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# TODO: Check transaction successful?
# Check that the user has inserted enough money to purchase the drink
# if the user has inserted enough money, then the cost of the drink gets added to the machine
# as the profit and this will be reflected the next time “report”
# If the user has inserted too much money, the machine should offer change.
# TODO: Make Coffee.
# If the transaction is successful and there are enough resources to make the drink the user selected,
# then the ingredients to make the drink should be deducted from the coffee machine resources.
# Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
# If latte was their choice of drink.

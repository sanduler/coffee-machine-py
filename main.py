# Ruben Sanduleac
# Date: January 26th, 2022
# Description: This program simulates a coffee machine where the user
#              places a specific amount and selects a drink. If the amount is
#              is over the needed amount the sum is refunded.

# TODO: Prompt user by asking "What would you like? (espresso/latte/cappuccino):”
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

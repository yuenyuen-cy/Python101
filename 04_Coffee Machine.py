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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

money = 0

# TODO 3. Print report.

def generate_report():
    """Generate a printed report if user selects report"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")


def check_sufficient(drink):
    """Check if there are sufficient resources to make the selected drink"""
    ingredients_needed = MENU[drink]["ingredients"]

    for item, requirement in ingredients_needed.items():
       if resources.get(item) < requirement:
           print(f"Sorry there is not enough {item}. Please make another selection.")
           return False
    return True

# TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"

machine_on = True

while machine_on:

    user_action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drink_choices = ["espresso", "latte", "cappuccino"]

    # TODO 2. Turn off the Coffee Machine by entering "off" to the prompt.

    if user_action == "off":
        machine_on = False

    elif user_action == "report":
        generate_report()

    elif user_action in drink_choices:

    # TODO 4. Check resources sufficient?

        if check_sufficient(user_action):

            # TODO 5. Process coins.

            print("Please insert coins.")
            quarter_inserted = int(input("How many quarters: "))
            dimes_inserted = int(input("How many dimes: "))
            nickles_inserted = int(input("How many nickles: "))
            pennies_inserted = int(input("How many pennies: "))

            value_coins = (quarter_inserted * coins["quarters"]) + (dimes_inserted * coins["dimes"]) + (
                        nickles_inserted * coins["nickles"]) + (pennies_inserted * coins["pennies"])
            return_change = value_coins - MENU[user_action]["cost"]

            # TODO 6. Check transaction successful?
                ## sufficient resources
                ## enough $$

            if return_change >= 0:
                print(f"Here is ${round(return_change, 2)} in change.")

                money += MENU[user_action]["cost"]

                for ingredient, amount_needed in MENU[user_action]["ingredients"].items():
                    resources[ingredient] -= amount_needed

                # TODO 7. Make Coffee.

                print(f"Here is your {user_action}. Enjoy!")

            else:
                print("Sorry, that's not enough money. Money refunded.")

    else:
        print("Invalid input. Please select again.")
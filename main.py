MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "ingredients": {
        "water": [300, "ml"],
        "milk": [200, "ml"],
        "coffee": [100, "g"],
    },
    "money": [0, "$"],
}


def print_report():
    for item in resources["ingredients"]:
        print(f"{item}: {resources["ingredients"][item][0]}{resources["ingredients"][item][1]}")
    print(f"money: {resources["money"][0]}{resources["money"][1]}")


def check_resources(coffee_type):
    coffee_type = MENU[coffee_type]
    for item in coffee_type["ingredients"]:
        if resources["ingredients"][item][0] < coffee_type["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins(coffee_type):
    coffee_type = MENU[coffee_type]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_sum = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total_sum < coffee_type["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    resources["money"][0] += coffee_type["cost"]
    if total_sum > coffee_type["cost"]:
        change = total_sum - coffee_type["cost"]
        print(f"Here is ${change:.2f} dollars in change.")
    return True


def make_coffee(coffee_type):
    coffee_info = MENU[coffee_type]
    for item in coffee_info["ingredients"]:
        resources["ingredients"][item][0] -= coffee_info["ingredients"][item]
    print(f"Here is your {coffee_type} Enjoy!")


def coffee():
    while True:
        user_choice = input(f"What would you like (espresso/latte/cappuccino):").lower()
        match user_choice:
            case "report":
                print_report()
            case "off":
                exit(0)
            case _:
                if user_choice in ["espresso", "latte", "cappuccino"]:
                    if not check_resources(user_choice):
                        continue
                    if process_coins(user_choice):
                        make_coffee(user_choice)


if __name__ == "__main__":
    coffee()

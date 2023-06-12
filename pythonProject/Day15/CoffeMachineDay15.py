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

profit = 0

# TODO 1: Ask the user what he wants to drink

# input("What would you like? (espresso/latte/cappuccino): " ).lower()



def check_resources(choice, machine_resources):
    ''' Checks if resources are suffcient '''

    for resource in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients'][resource] > machine_resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def take_money():
    '''Asks the client to insert coins'''
    user_total = 0.25 * int(input("how many quarters? "))
    user_total += 0.1 * int(input("how many dimes? "))
    user_total += 0.05 * int(input("how many nickles? "))
    user_total += 0.01 * int(input("how many pennies? "))

    return round(user_total, 2)


def make_beverage(choice, resources,profit):
    for resource in MENU[choice]['ingredients']:
        resources[resource] = resources[resource] - MENU[choice]['ingredients'][resource]
    print(f"Here is your {choice}🥃 Enjoy!")
    return resources


def report(resources):
    for resource in resources:
        if resource == 'coffee':
            print(f"{resource}: {resources[resource]}gr")
        else:
            print(f"{resource}: {resources[resource]}ml")
    print(f"Money: ${profit}")


def start_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    game_on = True
    while game_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'espresso' or user_choice ==  'latte' or user_choice ==  'cappuccino':
            check = check_resources(user_choice, resources)
            if check:
                print("Please insert coins.")
                beverage_cost = MENU[user_choice]['cost']
                client_money = take_money()
                if client_money >= beverage_cost:
                    client_money -= beverage_cost
                    global profit
                    profit += beverage_cost
                    print(f"Here is ${client_money} in change.")
                    resources_left = make_beverage(user_choice, resources,profit)
        elif user_choice == "off":
            return 0
        elif user_choice == 'report':
            report(resources)


start_machine()

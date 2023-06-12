from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
maker = CoffeeMaker()

in_line = True
while in_line:
    choice = input(f"What would you like? {menu.get_items()} : ").lower()
    if choice == 'report':
        maker.report()
        money.report()
    elif choice == 'off':
        in_line = False
    else:
        if choice in menu.get_items():
            drink = menu.find_drink(choice)
            if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                maker.make_coffee(drink)
        else:
            print("Sorry that item is not available.")



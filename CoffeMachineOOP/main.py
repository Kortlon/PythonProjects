from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
#menu_item = MenuItem()
list = menu
coffe_on = True
while coffe_on:
    check_drink = False
    while check_drink == False:
        user_drink = input("What would you like to drink? " + menu.get_items() + ": ").lower()
        if user_drink == 'report':
            coffee_maker.report()
            money.report()
        elif user_drink == 'off':
            coffe_on = False
            check_drink = True
        elif menu.find_drink(user_drink) is not None:
            drink = menu.find_drink(user_drink)
            if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                check_drink = True




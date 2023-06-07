import menu

print(menu.MENU)

machine_water = menu.resources['water']
machine_milk = menu.resources['milk']
machine_coffe = menu.resources['coffee']
machine_money = 0  # $
machine_run = True

print(menu.MENU['espresso']['cost'])
print(menu.MENU['espresso']['ingredients']['water'])


def checkingridents(item):
    choice = menu.MENU[item]['ingredients']
    water = choice['water']
    coffee = choice['coffee']
    checker = 0

    if machine_water < water:
        print("Not Enough Water")
        checker += 1
    if machine_coffe < coffee:
        print("Not Enough Coffee")
        checker += 1
    if 'milk' in choice:
        milk = choice['milk']
        if machine_milk < milk:
            print("Not Enought Milk")
            checker += 1
    return checker


def calcmoney():
    q = int(input("How many quaters?:"))
    d = int(input("How many dimes?:"))
    n = int(input("How many nickles?:"))
    p = int(input("How many pennies?:"))
    sum = 0
    sum += q * .25
    sum += d * .10
    sum += n * .05
    sum += p * .01
    return sum


def checkuser(input):
    if input == 'espresso' or input == 'latte' or input == 'cappuccino':
        return 'ready'
    elif input == 'report':
        print(f"Water: {machine_water}")
        print(f"Coffee: {machine_coffe}")
        print(f"Milk: {machine_milk}")
    else:
        print("Not a Valid Option")


while machine_run == True:
    user_option = ''
    while user_option != 'ready':
        user_choice = str(input("What would you like? (expresso/latte/cappuccino):")).lower()
        user_option = checkuser(user_choice)
        can_afford = True
    while can_afford == True:
        supply = checkingridents(user_choice)
        print(supply)
        if supply == 0:
           print("Please insert coin.")
           user_money = calcmoney()
           item_cost = int(menu.MENU[user_choice]['cost'])
           if user_money > item_cost:
               user_change = user_money - item_cost
               if user_change > 0:
                   print(f"Here is ${user_change:.2f} in change")
           if user_money < item_cost:
               print("Sorry that's not enough money. Money refunded.")
               can_afford = False




    machine_run = False

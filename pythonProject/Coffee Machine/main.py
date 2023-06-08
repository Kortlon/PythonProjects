import menu

#print(menu.MENU)

machine_water = menu.resources['water']
machine_milk = menu.resources['milk']
machine_coffe = menu.resources['coffee']
machine_money = 0.00  # $
machine_run = True

print(menu.MENU['espresso']['cost'])
print(menu.MENU['espresso']['ingredients']['water'])


def checkingridents(item):
    choice = menu.MENU[item]['ingredients']
    water = choice['water']
    coffee = choice['coffee']
    checker = 0

    if machine_water < water:
        print("Sorry there is Not Enough Water")
        checker += 1
    if machine_coffe < coffee:
        print("Sorry there is Not Enough Coffee")
        checker += 1
    if 'milk' in choice:
        milk = choice['milk']
        if machine_milk < milk:
            print("Sorry there is Not Enought Milk")
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

def use_milk(item, machine_cost):
    if 'milk' in menu.MENU[item]['ingredients']:
        use_milk =int(menu.MENU[item]['ingredients']['milk'])
        milk_left = machine_cost - use_milk
        return milk_left
    else:
        milk_left = machine_cost
        return milk_left

def use_water(item, machine_cost):
    use_water = int(menu.MENU[item]['ingredients']['water'])
    water_left = machine_cost - use_water
    return water_left

def use_coffee(item, machine_cost):
    use_coffee = int(menu.MENU[item]['ingredients']['coffee'])
    coffee_left = machine_cost - use_coffee
    return coffee_left

def checkuser(input):
    if input == 'espresso' or input == 'latte' or input == 'cappuccino':
        return 'ready'
    elif input == 'report':
        print(f"Water: {machine_water}ml")
        print(f"Coffee: {machine_coffe}g")
        print(f"Milk: {machine_milk}ml")
        print(f"Money: ${machine_money:.2f}")
    else:
        print("Not a Valid Option")


while machine_run == True:
    user_option = ''
    while user_option != 'ready':
        user_choice = str(input("What would you like? (espresso/latte/cappuccino):")).lower()
        user_option = checkuser(user_choice)
        can_afford = True
    while can_afford == True:
        supply = checkingridents(user_choice)
        if supply == 0:
           print("Please insert coin.")
           user_money = calcmoney()
           item_cost = float(menu.MENU[user_choice]['cost'])
           if user_money >= item_cost:
               user_change = user_money - item_cost
               if user_change > 0:
                   machine_money += item_cost
                   print(f"Here is ${user_change:.2f} in change")
                   machine_water = use_water(user_choice, machine_water)
                   machine_coffe = use_coffee(user_choice, machine_coffe)
                   machine_milk = use_milk(user_choice, machine_milk)
                   print(f"Here is your {user_choice}☕ Enjoy!")
                   can_afford = False
           if user_money < item_cost:
               print("Sorry that's not enough money. Money refunded.")
               can_afford = False
        if supply > 0:
            can_afford = False








    machine_run = True

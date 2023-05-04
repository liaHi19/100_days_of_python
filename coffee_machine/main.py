from data import MENU, resources
money = 0
is_on = True


def process_coins(order, money):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.5
    pennies = int(input("How many pennies?: ")) * 0.1

    sum_coins = sum([quarters, dimes, nickles, pennies])
    drink_cost = MENU[order]["cost"]

    if drink_cost > sum_coins:
        print("Sorry there is not enough coins")
        return False
    else:
        change = round(sum_coins - drink_cost, 2)
        money += drink_cost
        # make coffee
        print(f"Here is your change S{change}")
        print(f"Here is your {order}. Enjoy!")
        return True


def check_ingredients(order, resources):
    drink_data = MENU[order]["ingredients"]
    for resource in resources:
        if resources[resource] < drink_data[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
        else:
            return process_coins(order, money)
                

while is_on:
    order = input('''What would you like? 
    (espresso - $1.5/latte - $2.5 /cappuccino - $3): ''').lower()

    drink = ""
    for item in MENU:
        if order == item:
            drink = item
    if order == "off":
        is_on = False
    elif order == "report":
        for resource in resources:
            ingredient = str(resources[resource]).title()
            if resource == "coffee":
                ingredient += "g"
            else: 
                ingredient += "ml"
                print(f"{resource}: {ingredient}")
            print(f"Money: ${money}")
    
    elif order == drink and drink != "":
        check_ingredients(order, resources)
    else:
        print("Please enter valid drink")
        is_on = False



    

from data import MENU, resources
money = 0
is_on = True


def make_coffee(order):
    drink_data = MENU[order]["ingredients"]
    for item in drink_data:
        resources[item] -= drink_data[item]


def check_transaction(total, order):
    global money
    drink_cost = MENU[order]["cost"]
     
    if drink_cost > total:
        print("Sorry there is not enough coins")
        return False
    else:
        change = round(total - drink_cost, 2)
        money += drink_cost
        print(f"Here is your change S{change}")
        print(f"Here is your {order}. Enjoy!")
        return make_coffee(order)


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.5
    total += int(input("How many pennies?: ")) * 0.1
    
    return total
   

def check_ingredients(order):
    drink_data = MENU[order]["ingredients"]
    for resource in resources:
        if resources[resource] < drink_data[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
        else:
            return True
            
          
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
            ingredient = str(resources[resource])
            if resource == "coffee":
                ingredient += "g"
            else: 
                ingredient += "ml"
            print(f"{resource}: {ingredient}")
        print(f"Money: ${money}")
    
    elif order == drink and drink != "":
        if check_ingredients(order):
            check_transaction(process_coins(), order)
    else:
        print("Please enter valid drink")
        is_on = False
from data import MENU, resources
is_working = True


def work_coffee_machine():

    order = input('''What would you like? 
    (espresso - $1.5/latte - $2.5 /cappuccino - $3): ''').lower()
    money = 0

    drink = ""
    for item in MENU:
        if order == item:
            drink = item
            print(drink)

    def check_ingredients(order, resources):
        drink_data = MENU[order]["ingredients"]
        for resource in resources:
            if resources[resource] < drink_data[resource]:
                print(f"Sorry there is not enough {resource}.")
                return 
            
    if order == "report":
        for resource in resources:
            ingredient = str(resources[resource])
            if resource == "coffee":
                ingredient += "g"
            else: 
                ingredient += "ml"
            print(f"{resource}: {ingredient}")
        print(f"money: ${money}")
    elif order == "off":
        return
    elif order == drink and drink != "":
        return check_ingredients(order, resources)
    else:
        print("Please enter valid drink")
        return


work_coffee_machine()

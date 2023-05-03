from data import MENU, resources

order = input("What would you like? (espresso - $1.5/latte - $2.5 /cappuccino - $3): ")
money = 0

for item in MENU:
    if order == item:
        print(item)


if order == "report":
    for resource in resources:
        ingredient = str(resources[resource])
        
        if resource == "coffee":
            ingredient += "g"
        else: 
            ingredient += "ml"
        
        print(f"{resource}: {ingredient}")
    print(f"money: ${money}")


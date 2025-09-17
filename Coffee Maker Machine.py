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
money=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please enter coins:")
    total = int(input("quarters:"))*0.25
    total += int(input("dimes:"))*0.10
    total += int(input("nickels:"))*0.05
    total += int(input("pennies:"))*0.01
    return total

def transaction_successful(money_recieved,actual_drink_cost):
    if money_recieved >= actual_drink_cost:
        change = round(money_recieved - actual_drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += actual_drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️. Enjoy!")

coffee_machine_is_on = True

while coffee_machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        coffee_machine_is_on == False
    elif choice == "report":
        print(f"Water:{resources["water"]}ml")
        print(f"Milk :{resources["milk"]}ml")
        print(f"Coffee:{resources["coffee"]}g")
        print(f"Money:${money}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

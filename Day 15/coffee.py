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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough_resources(order_ingreients):
    for item in order_ingreients:
        if order_ingreients[item] >= resources[item]:
            print(f"Sorry there's not enough {item}")
            return False
    return True     

def process_coins():
    '''returns total number of coins inserted'''
    print('insert your coins')
    total = int(input('how many quarters: ')) * 0.25
    total += int(input('how many dimes: ')) * 0.1
    total += int(input('how many nickels: ')) * 0.05
    total += int(input('how many pennies: ')) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")    
        return False
def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your {drink_name}. Enjoy!!!")    

#def report():
is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit} ") 
    else:
        drink = MENU[choice]
        if is_enough_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])

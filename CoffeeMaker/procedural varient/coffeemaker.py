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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 3. Print report.
def reduce(user_choice):
    """reduce the resources after successfull order"""
    order = MENU[user_choice]["ingredients"]
    for item in order:
        resources[item]-=order[item]
    

def report(collection):
    """ returns the remaining resources"""
    for item in resources:
        print(f"{item} : {resources[item]}")
    print(f"Money : ${collection}")


# TODO 4. Check resources sufficient?


def is_sufficient(user_choice):
    """returns boolean, Resource is sufficient or not"""
    order = MENU[user_choice]["ingredients"]
    for item in order:
        if order[item] > resources[item] :
           return False
    return True


# TODO 5. Process coins.

def coins():
    """ask the inputs and returns total value of coins"""
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return money


device = True
collection = 0

while device:
    # TODO 1 1. Prompt user by asking “ What would you like?
    user_choice = input("' What would you like? (espresso/latte/cappuccino): '").lower()
    # TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    # TODO 6. Check transaction successful?
    if user_choice == 'off':
        device = False
    elif user_choice != 'report':
        cost = MENU[user_choice]['cost']
        sufficient = is_sufficient(user_choice)
        if sufficient:
            coin = coins()
            if coin > cost :
                remain = coin - cost
                print(f"Here's your change {round(remain, 2)}")
            if coin >= cost:
                print(f"Here is your {user_choice}☕. Enjoy!")
                if coin == cost:
                    collection += coin
                elif coin > cost:
                    collection += cost
                reduce(user_choice)
            elif coin < cost:
                print(f"Sorry that's not enough money. Money refunded.")
        else:
            print("sorry, ingredients ran out")
    elif user_choice == 'report':
        report(collection)
    






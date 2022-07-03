import collections
from doctest import REPORT_CDIFF
from gc import collect
from os import supports_effective_ids
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
machine = True
collection = 0
while machine :
    order = input("What would you like? " + menu.get_items() +' ').lower()
    if order == "off":
        machine = False
    elif order == "report":
        coffeemaker.report()
        moneymachine.report()
    else :
        order_items = menu.find_drink(order)
        if order_items != None:
            is_sufficient = coffeemaker.is_resource_sufficient(order_items)
            if is_sufficient :
                cost = order_items.cost
                payment = moneymachine.make_payment(cost)
                if payment :
                    coffeemaker.make_coffee(order_items)
            else:
                print("")
        

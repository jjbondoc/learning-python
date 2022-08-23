# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# #* Initialising a Screen object called my_screen
# my_screen = Screen()
# print(my_screen.canvheight) # canvheight is an attribute
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align = 'l'
# print(table.align)
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
cash = MoneyMachine()

while True:
    answer = input("What would you like? (espresso/latte/cappuccino/): ")
    if answer == 'off':
        exit(0)
    elif answer == 'report':
        machine.report()
        cash.report()
    elif answer in menu.get_items():
        order = menu.find_drink(answer)
        if machine.is_resource_sufficient(order) and cash.make_payment(order.cost):
            machine.make_coffee(order)
    else:
        print("Invalid order, please try again.")
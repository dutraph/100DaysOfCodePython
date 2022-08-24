from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
report = CoffeeMaker().report()
answer = input(f"What would you like? ({menu.get_items()}): ").lower()
if answer == 'report':
    print(report)
elif answer == 'off':
    print("Turning the machine off...")
    print("Bye! 😜")

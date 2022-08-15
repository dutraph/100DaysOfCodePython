from coffe_data import resources, MENU
import time
profit = 0.0


def add_money(coffee_cost):
    global profit
    profit += coffee_cost


def menu():
    print("Turning the machine on, warming up!")
    time.sleep(2)
    print("Almost there!")
    time.sleep(2)
    print("Here we go....")
    time.sleep(1)
    should_stop = False
    while not should_stop:
        answer = input("What would you like? (espresso / latte / cappuccino): ").lower()
        if answer == 'report':
            print(report())
        elif answer == 'off':
            print("Turning the machine off...")
            time.sleep(2)
            print("Bye! 😜")
            break
        elif answer == 'espresso' or answer == 'latte' or answer == 'cappuccino':
            if check_resources(answer) != 0 and process_coins(answer) != 0:
                make_coffee(answer)
        else:
            print("Invalid Option!")


def resource(r):
    return resources[r]


def process_coins(coffee):
    print("Please insert the coins.")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickles = int(input("Nickles: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    coffee_cost = MENU[coffee]['cost']
    coins_sum = quarters + dimes + nickles + pennies
    if coins_sum < coffee_cost:
        print("Sorry, Not enough money, money refunded! ")
        return 0
    else:
        if coins_sum == coffee_cost:
            print("Please proceed!")
            add_money(coffee_cost)
            return 1
        elif coins_sum > coffee_cost:
            change = coins_sum - coffee_cost
            print(f"Here's your change: ${change:.2f}")
            add_money(coffee_cost)
            return 1


def report():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit:.2f}"


def check_resources(coffee):
    chk = []
    for r in MENU[coffee]['ingredients']:
        if resources[r] - MENU[coffee]['ingredients'][r] <= 0:
            chk.append(False)
    if False in chk:
        print(f"Sorry there is not enough resources for a {coffee}")
        return 0
    else:
        return 1


def make_coffee(coffee):
    for r in MENU[coffee]['ingredients']:
        resources[r] -= MENU[coffee]['ingredients'][r]
    print(f"Here's your {coffee}, enjoy it! ☕")


menu()


# TODO: 1. Print report of all coffee machine resources.
# TODO: 2. Check resources sufficient to make drink order.

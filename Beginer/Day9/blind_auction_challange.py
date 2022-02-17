# import only system from os
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')  # for windows
    else:
        _ = system('clear')  # for mac and linux(here, os.name is 'posix')


def find_highest_bid(bid_dict):
    message = ''
    highest_bid = 0
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            message = f'The winner was {bidder}: ${highest_bid}.'
    return message


bidders = {}
bidder_joining = True
clear()
while bidder_joining:    
    name = input("What's your name: ")
    bid = float(input("What's your bid: $"))
    bidders[name] = bid
    joiner = int(input("Are there any other bidders: 1=yes 2=no: "))
    if joiner == 2:
        bidder_joining = False
    elif joiner == 1:
        clear()

print(find_highest_bid(bidders))

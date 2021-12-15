import random
from random import randint


def rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)


def paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


def scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


player = int(input("Enter 1=Rock / 2=Paper / 3=Scissors: "))
game = [rock(), paper(), scissors()]
player_hand = game[player - 1]
cpu = random.choice(game)

print("You Choose")
print(player_hand)

print()
print()

print("CPU Choose")
print(cpu)
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


def chosen_hand(pve, name):
    if pve == 1:
        print(f"{name} choose rock")
        rock()
    elif pve == 2:
        print(f"{name} choose paper")
        paper()
    elif pve == 3:
        print(f"{name} choose scissors")
        scissors()


player = int(input("Enter 1=Rock / 2=Paper / 3=Scissors: "))
chosen_hand(player, "You")
print()
print()
cpu = randint(1, 3)
chosen_hand(cpu, "CPU")


if player == cpu:
    print("it's a draw")
if player == 1 and cpu == 2:
    print("cpu wins")
elif player == 1 and cpu == 3:
    print("you win")
elif player == 2 and cpu == 1:
    print("you win")
elif player == 2 and cpu == 3:
    print("cpu wins")
elif player == 3 and cpu == 1:
    print("you win")
elif player == 3 and cpu == 2:
    print("you win")


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
cpu = randint(1,3)

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

chosen_hand(player, "Paulo")
chosen_hand(cpu, "CPU")

if player == 1 and cpu == 3:
    print("You win!")
elif cpu > player:
    print("You lose!")
elif cpu == player:
    print("It's a draw!")
else:
    print("you typed an invalid number, you lose!")
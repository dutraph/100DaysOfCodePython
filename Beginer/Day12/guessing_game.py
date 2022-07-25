from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


# class Difficulty:
#     def __init__(self, difficulty):
#         self.difficulty = difficulty
#
#     @property
#     def difficulty(self):
#         return self.difficulty
#
#     @difficulty.setter
#     def difficulty(self, difficulty):
#         self.difficulty = difficulty
#
#     def __int__(self):
#         return int(self.difficulty)
#

def set_difficulty():
    difficulty = int(input("Choose a difficulty: 1=Easy / 2=Hard: "))
    if difficulty == 2:
        return HARD_LEVEL
    elif difficulty == 1:
        return EASY_LEVEL


def check_answer(number, chances):
    while not chances == 0:
        guess = int(input("Guess a number: "))
        if guess > number:
            print("Too High")
            chances -= 1
            print(f"You have {chances} left!")
        elif guess < number:
            print("Too low")
            chances -= 1
            print(f"You have {chances} left!")
        elif guess == number:
            print("You've got it")
            break
        elif chances == 0:
            print("You're running out of chances")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm Thinking a number between 1 and 100!")
    chances = set_difficulty()
    number = randint(0, 101)
    print(number)
    print(f"Your have {chances} attempts to guess the number. Good Luck!")
    check_answer(number, chances)
    replay = input("Play again? y/n: ")
    if replay == 'y':
        game()


game()

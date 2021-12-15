import random

names_list = input("Give me everybody's names, separated by a comma: ").split(", ")
# people = len(names_list) - 1
# who_will_pay = randint(0, people)
# print(f"{names_list[who_will_pay]} will pay the whole bill.")

# or

who_will_pay = random.choice(names_list)
print(f"{who_will_pay} will pay the whole bill.")

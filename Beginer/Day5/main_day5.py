import random

letters = int(input("How many letter you want: "))
password = ""
alphabet = ["a", "b", "c"]
for i in range(0, letters):
    password += random.choice(alphabet)

print(password)

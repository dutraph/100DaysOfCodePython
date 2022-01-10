import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '[', ']', '{', '}', '+', '^']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the password Generator!")
nb_letters = int(input("How many letters?\n"))
nb_symbols = int(input("How many symbols?\n"))
nb_numbers = int(input("How many numbers?\n"))


password_list = []
for l in range(0, nb_letters):
    password_list.append(random.choice(letters))

for s in range(0, nb_symbols):
    password_list.append(random.choice(symbols))

for n in range(0, nb_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print(password)

# np = ''.join(random.sample(password_list, len(password_list)))
# print(np)

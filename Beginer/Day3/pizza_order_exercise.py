print("Welcome to Python Pizza Deliveries")
size = input("Pizza size [s, m or l]: ")
add_pepperoni = input("add pepperoni [y/n]: ")
extra_cheese = input("add cheese [y/n]: ")

price = 0
# if size == 's':
#     price += 15
# elif size == 'm':
#     price += 20
# else:
#     price += 25
#
# if add_pepperoni == 'y' and size == 's':
#     price += 2
# elif (add_pepperoni == 'y' and size == 'm') or (add_pepperoni == 'y' and size == 'l') :
#     price += 3
# else:
#     price += 0
# if extra_cheese == 'y':
#     price += 1
# else:
#     price += 0

# print(f'your final bill is ${price:.2f}.')

if size == 's':
    price = 15
elif size == 'm':
    price = 20
elif size == 'l':
    price = 25
if add_pepperoni == 'y':
    if size == 's':
        price += 2
    else:
        price += 3
if extra_cheese == 'y':
    price += 1
print(f'your final bill is ${price:.2f}.')

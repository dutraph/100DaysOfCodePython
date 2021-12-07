print("Welcome to the Python Pizza Deliveries")


def size():
    pizza_size = input("Enter the pizza size [s / m / l]: ")
    while True:
        if pizza_size != "m" or pizza_size != "m" or pizza_size != 'l':
            pizza_size = input("Enter a valid size s, m or l: ")
        else:
            break
    return pizza_size


size()
#
# add_peperoni
# add_cheese

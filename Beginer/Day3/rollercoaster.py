print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))
ticket_price = 0.0
fee = 3.0
if height >= 120:
    print("you're allowed")
    age = int(input("What's your age: "))
    if age < 12:
        ticket_price = 5.0
        print("Child ticket price $5.0")
    elif age <= 18:
        ticket_price = 7.0
        print("Youth ticket price $7.0")
    else:
        ticket_price = 12.0
        print("Adult ticket price $12.0")
    picture = input("Do you want a picture during the trip? [y/n]: ")
    while True:
        if picture != "y" and picture != "n":
            picture = input("Please enter a valid input [y/n]: ")
        else:
            break
    if picture == "y":
        ticket_price += fee
        print(f"Total bill ${ticket_price}")
    else:
        print(f"Total bill ${ticket_price}")
else:
    print("You need to grow up first buddy!")

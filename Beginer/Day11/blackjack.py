import random


def deal_card():
    """"Return a random card from the deck"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


user_cards = []
cpu_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    cpu_cards.append(deal_card())


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def show_cards():
    print(f"User:{user_cards}")
    print(f"CPU:{cpu_cards}")


user_score = calculate_score(user_cards)
cpu_score = calculate_score(cpu_cards)


while (user_score or cpu_score) <= 21:
    print(f'Your cards{user_cards} = {user_score}')
    print(f'CPU cards{cpu_cards} = {cpu_score}')
    cpu_cards.append(deal_card())
    cpu_score = calculate_score(cpu_cards)
    new_card = input("want a new card (y/n)? ")
    if new_card == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)

    if user_score == cpu_score:
        print("Draw")
        show_cards()
        break
    elif cpu_score > 21 and user_score == 21:
        print("You Win")
        show_cards()
        print(f'User:{user_score} / CPU:{cpu_score}')
        break
    elif (user_score > 21) or (21 - user_score) > (21 - cpu_score):
        print("CPU Wins")
        show_cards()
        print(f'User:{user_score} / CPU:{cpu_score}')
        break




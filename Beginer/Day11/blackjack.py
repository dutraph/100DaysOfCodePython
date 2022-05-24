import random


def deal_card():
    """"Return a random card from the deck"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


user_cards = []
cpu_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)

soma = 0
game_over = False
while not game_over:
    card1 = deal_card()
    card2 = deal_card()
    soma = card2 + card1
    if soma <= 21:
        print(f'{card1}, {card2}')
        another_card = input("Want another card (y/n)? ")
        if another_card == 'y':
            card3 = deal_card()
            soma += card3
    else:
        game_over = True

print(soma)

# card1 = random.choice(cards)
# card2 = random.choice(cards)
#
# print(f"{card1} , {card2}")
#
#
# soma = card2 + card1
# print(f"[{card1}, {card2}] = {soma}")


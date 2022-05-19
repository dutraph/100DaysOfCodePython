import random

cards = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

higher_cards = {
    "A": 11,
    "J": 10,
    "Q": 10,
    "K": 10
}

card1 = random.choice(cards)
card2 = random.choice(cards)

print(f"{card1} , {card2}")

if type(card1) is not int:
    card1 = 10
elif type(card2) is not int:
    card2 = 10


soma = card2 + card1
print(f"[{card1}, {card2}] = {soma}")
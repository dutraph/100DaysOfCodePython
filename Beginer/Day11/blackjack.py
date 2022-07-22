import random


def deal_card():
    """"Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def cal_score(card_list):
    """Take a list of card and return the score calculated from the cards!"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(user_score, cpu_score):
    print()
    if user_score == cpu_score:
        return "Draw!!!"
    elif cpu_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score > 21:
        return "You went over, you lose."
    elif cpu_score > 21:
        return "Opponent went over, you win."
    elif user_score > cpu_score:
        return "You Win!"
    else:
        return "You Lose!"


def final_hand(user_score, cpu_score, user_cards, cpu_cards):
    print("FINAL HAND!!!")
    print(f'Your hand: {user_cards} - Score: {user_score}')
    print(f'Dealer hand: {cpu_cards} - Score: {cpu_score}')


def game():
    user_score = 0
    cpu_score = 0
    user_cards = []
    cpu_cards = []
    is_game_over = False

    for _ in range(2):  # '_' means that we don't need the variable, but we need the commands inside runs twice.
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())
    while not is_game_over:
        user_score = cal_score(user_cards)
        cpu_score = cal_score(cpu_cards)

        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'CPU first card: {cpu_cards[0]}')

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while cpu_score < 17 and cpu_score != 0:
        cpu_cards.append(deal_card())
        cpu_score = cal_score(cpu_cards)

    print(compare(user_score, cpu_score))
    final_hand(user_score, cpu_score, user_cards, cpu_cards)

    while input("Replay y/n: ") == "y":
        print(end='\n\n\n')
        game()


game()


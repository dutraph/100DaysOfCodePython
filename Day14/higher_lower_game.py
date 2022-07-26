import random
from art import logo, vs
from game_data import data
import os

b_turns_a = []


def cls():
    return os.system('cls')


def gen_chars():
    return random.choice(data)


def right_score_cheering():
    congrats = ["You're awsome!", "Good job!", "Marvelous!", "You're right!", "Got Skill bicth!", "Hell yeah!", "On Fire...", "It seems we have a Sherlok here..."]
    return random.choice(congrats)


def format_output(score, key, key2):
    if score > 0:
        print(f"{right_score_cheering()} your score: {score}")
    print(f"Compare A: {key['name']}, a {key['description']}, from {key['country']}")
    print(vs)
    print(f"Against B: {key2['name']}, a {key2['description']}, from {key2['country']}")
    print(f"A: {key['follower_count']} / B: {key2['follower_count']}")


def game():
    cls()
    char_a = gen_chars()
    char_b = gen_chars()
    score = 0
    keep_playing = True
    while keep_playing:
        if char_a == char_b:
            char_b = gen_chars()
        print(logo)
        a_win = char_a['follower_count'] > char_b['follower_count']
        b_win = char_a['follower_count'] < char_b['follower_count']
        format_output(score, char_a, char_b)
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (a_win and choice == 'a') or (b_win and choice == 'b'):
            b_turns_a.append(char_b)
            score += 1
            char_a = b_turns_a[-1]
            char_b = gen_chars()
            cls()
        else:
            cls()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False
            replay = int(input("Wanna play again? 1=yes 2=no: "))
            if replay == 1:
                game()
            else:
                break


game()

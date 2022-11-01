from pydoc import describe
import random
from art import logo, vs
from game_data import data


def random_karakter():
    return random.choice(data)


def account_name(karakter):
    acount_name = karakter['name']
    acount_description = karakter['description']
    acount_country = karakter['country']
    return f"{acount_name}, {acount_description}, {acount_country}"


def count_result(guess, a, b):
    if a > b:
        return guess == 'a'
    else:
        return guess == 'b'


print(logo)
game_end = True
b = random_karakter()
score = 0

while game_end:

    a = b
    b = random_karakter()

    if a == b:
        b = random_karakter()

    print(f"Compare A : {account_name(a)}")
    print(vs)
    print(f"Compare B : {account_name(b)}")

    guess = input("Who has more followers ? type 'A' or 'B': ").lower()
    count_a = a['follower_count']
    count_b = b['follower_count']
    is_correct = count_result(guess, count_a, count_b)
    
    if is_correct:
        score += 1
        print(f"your score : {score}")
    else:
        game_end = False
        print(f"Sorry, that's wrong. final score : {score}")

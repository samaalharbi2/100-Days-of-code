## Day 14 - Section 14: Beginner - Higher Lower Game
import random
from higher_lower_data import data
from higher_lower_logo import logo, vs

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name,description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess,a_followers,b_followers):
    """Checks followers against user guess
    and return true if they got it right
    or false if they got it wrong"""
    if a_followers > b_followers:
        return guess == "a"

    else:
        return guess == "b"

def game():
    """Game machanics"""
    print(logo)
    score = 0
    game_should_countinue =True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_countinue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}. ")

        guess = input("Who has more followers? Type 'A' or 'B' :").lower()
        a_followers_count = account_a["follower_count"]
        b_followers_count = account_b["follower_count"]
        is_correct = check_answer(guess,a_followers_count,b_followers_count)

        print(logo)
        if is_correct:
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_countinue = False
            print(f"Sorry, that's wrong.Final score: {score}")

game()





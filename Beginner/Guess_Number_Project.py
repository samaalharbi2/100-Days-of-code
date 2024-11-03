## Day 12 - Section 12: Beginner - Number Gussing Game
import random
import guess_the_number_art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to check users' guess against actual answer

def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess, returns the number of turns remanining"""
    if user_guess > actual_answer:
        print("Too Hight")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! the answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choso a difficulty. Type 'easy' or 'Hard' ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(guess_the_number_art.logo)
#Choosing a random number between 1 and 100.
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Passt, the correct answer is {answer}")

    turns = set_difficulty()

    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        # Let the user guess a number
        guess = int(input('Make a Guess: '))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()








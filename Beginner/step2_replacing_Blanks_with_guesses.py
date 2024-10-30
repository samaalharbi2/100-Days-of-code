#python list
import random

word_list = ["aardvark","baboon","camel"]

# TODO 1-
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO 2-
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO 3-
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
       display += "_"

print(display)
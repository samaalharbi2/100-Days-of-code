import random

# List of letters, numbers, and symbols for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbol = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', "$", "&", "#", "@"]

print("Welcome to the PyPassword Generator!")  # Welcome message
# Get user input for the number of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to hold the password characters
password_list = []

# Add random letters to the password list
for char in range(nr_letters):
    password_list.append(random.choice(letters))
# Add random numbers to the password list
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))
# Add random symbols to the password list
for char in range(nr_symbol):
    password_list.append(random.choice(symbol))

# Print the password list (for debugging purposes)
print(password_list)

# Shuffle the password list to randomize the order of characters
random.shuffle(password_list)

# Print the shuffled password list (for debugging purposes)
print(password_list)

# Join the list into a single string for the final password
password = ""
for char in password_list:
    password += char

# Print the final password
print(f"Your password is: {password}")





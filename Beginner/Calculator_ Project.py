## Day 10 - Section 10: Beginner - calculator project

import calculator_art

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multipy(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multipy,
    "/" : divide
}

def calculator():
    print(calculator_art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number? "))

    while should_accumulate:
        for symble in operation:
            print(symble)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to countinue calculating with {answer} or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

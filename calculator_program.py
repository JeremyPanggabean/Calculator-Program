# import art modul from art.py file
import art

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply, and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](12, 5))
def calculator():
    print(art.logo)
    print("Welcome to the Calculator Program!")
    num1 = float(input("What is the first number?: "))

    should_accumulate = True

    while should_accumulate:
        for symbol in operations.keys():
            print(symbol)
        while True:
            operation_symbol = input("Pick an operation: ")
            if operation_symbol in operations:
                break
            else:
                for symbol in operations.keys():
                    print(symbol)
                print("Invalid operation, Please choose from the available operations above.")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        if answer == 0.0:
            answer = 0
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'exit' to close the calculator program: ").lower()

        if choice == 'y':
            num1 = answer
        elif choice == 'exit':
            print("Thankyou for using the Calculator Program!")
            break
        else:
            should_accumulate = False
            print("\n" * 30)
            calculator()

calculator()
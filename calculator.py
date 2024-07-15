# Calculator program
from logo_art import logo
from decimal import Decimal

def add(first_number, second_number):
    """add the two numbers and return the result."""
    result_add = first_number + second_number
    return result_add


def subtract(first_number, second_number):
    """subtract the second number from the first number."""
    result_subtract = first_number - second_number
    return result_subtract


def multiply(first_number, second_number):
    """multiply the first number by the second number and return the result."""
    result_multiply = first_number * second_number
    return result_multiply


def divide(first_number, second_number):
    """divide the first number by the second number, if the second_number equals 0, print a message.
    Return the result."""
    if second_number == 0:
        print("invalid number for divisor.")
    result_divide = first_number / second_number
    return result_divide


calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def show_operations():
    """Display the available operations to user."""
    for key in calculator_operations:
        print(key)


def calculator():
    print(logo)
    first_num = Decimal(input("What is the first number?:"))
    show_operations()

    should_continue = True

    while should_continue:
        picked_operation = input("Pick an operation: ")
        second_num = Decimal(input("What is the second number?: "))
        calculation_function = calculator_operations[picked_operation]

        answer = calculation_function(first_num, second_num)

        print(f"{first_num} {picked_operation} {second_num}  = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation :") == 'y':
            first_num = answer
        else:
            should_continue = False
            calculator()


calculator()









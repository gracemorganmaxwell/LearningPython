"""
Assignment: IT6033 - Assignment 1
Task 1: Expression Validation
Student: 20200261, G Morgan-Maxwell
Accompaniment documentation in file: task1ReadME.md
"""


def ExpValidator(expression, openingChar, closingChar):
    """
    Validates if brackets in an expression match correctly.

    Args:
        expression (str): The expression to validate.
        openingChar (str): The opening character (e.g., '(').
        closingChar (str): The closing character (e.g., ')').

    Returns:
        str: "correct" if brackets match, "incorrect" otherwise.
    """
    stack = []  # Create an empty stack to track opening brackets.

    for char in expression:
        if char == openingChar:
            stack.append(char)  # Adding opening brackets to the stack.
        elif char == closingChar:
            if not stack:
                return "incorrect"  # There's a closing bracket without any opening bracket.
            if stack.pop() != openingChar:
                return "incorrect"  # The last opening bracket does not match the closing bracket.

    # After processing the expression, if the stack is empty, it's correct.
    if not stack:
        return "correct"
    else:
        return "incorrect"


def main():
    print("Welcome to Gracie's Expression Validating program in Python.")

    while True:
        # Prompting the user to input an expression for bracket matching.
        expression = input("Please enter your expression: ")

        # Asking the user for the bracket characters to match in the expression.
        bracketCharsInput = input("Enter the opening and closing characters to validate (e.g., < and > without "
                                  "quotes): ")

        # Parse the bracket characters input
        try:
            openingChar, closingChar = [char.strip() for char in bracketCharsInput.split(' and ')]
        except ValueError:
            print("Invalid input format. Please use the format: < and > without quotes.")
            continue

        # Calling the ExpValidator function and displaying the result.
        result = ExpValidator(expression, openingChar, closingChar)

        if result == "correct":
            print("Valid Expression.")
        else:
            print("Invalid Expression.")

        tryAgain = input("Do you want to try again? (Y/N): ")
        if tryAgain.lower() != 'y':
            print("Bye Bye!!")
            break


if __name__ == "__main__":
    main()

"""
Assignment: IT6033 - Assignment 1
Task 1: Expression Validation
Student: 20200261, G Morgan-Maxwell
Accompaniment documentation in file: task1ReadME.md
"""
def ExpValidator(expression, opening_char, closing_char):
    """
    Validates if brackets in an expression match correctly.

    Args:
        expression (str): The expression to validate.
        opening_char (str): The opening character (e.g., '(').
        closing_char (str): The closing character (e.g., ')').

    Returns:
        str: "correct" if brackets match, "incorrect" otherwise.
    """
    stack = []  # Create an empty stack to track opening brackets.

    for char in expression:
        if char == opening_char:
            stack.append(char)  # Adding opening brackets to the stack.
        elif char == closing_char:
            if not stack:
                return "incorrect"  # There's a closing bracket without any opening bracket.
            if stack.pop() != opening_char:
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
        bracket_chars_input = input("Enter the opening and closing characters to validate (e.g., < and > without "
                                    "quotes): ")

        # Parse the bracket characters input
        try:
            opening_char, closing_char = [char.strip() for char in bracket_chars_input.split(' and ')]
        except ValueError:
            print("Invalid input format. Please use the format: < and > without quotes.")
            continue

        # Calling the ExpValidator function and displaying the result.
        result = ExpValidator(expression, opening_char, closing_char)

        if result == "correct":
            print("Valid Expression.")
        else:
            print("Invalid Expression.")

        try_again = input("Do you want to try again? (Y/N): ")
        if try_again.lower() != 'y':
            print("Bye Bye!!")
            break


if __name__ == "__main__":
    main()

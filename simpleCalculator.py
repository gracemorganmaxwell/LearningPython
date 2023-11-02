"""Simple Calculator in Python Script, instructions: 1. Enter a first number, push the 'Enter' button.
2. Choose and enter your operator ( i.e. addition, minus, divide etc.), again push 'Enter'.
3. Enter a second number, and push 'Enter'.
4. The calculator should now display the result for you.
"""

# ---- project code below ----
# declaring the functions
def add(x, y):
    # functions body
    """
        Function Name: add
        Parameters: x, y - numbers to be added.
        Returns: Sum of x and y.
        """
    return x + y  # optional return statement

# FUNCTIONS: Functions are reusable pieces of code. They execute when called by name.
# They can have inputs (parameters) and return outputs (results).

def subtract(x, y):
    """Returns the difference between x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """
      Returns the result of dividing x by y.
      A CONDITIONAL inside checks for division by zero to avoid errors.
      """
    if y == 0:  # CONDITIONAL: Executes the block of code inside if the condition (y == 0) is true.
        return "Undefined (division by zero)"
    return x / y

def main():
    # Prompt user for input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator(+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on the operator
    # CONDITIONAL STATEMENTS: Check the value of 'operator' and call the appropriate function.
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":  # 'elif' is short for 'else if'. It checks another condition if the previous was false.
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":  # If none of the above conditions are true, the 'else' block executes.
        result = divide(num1, num2)
    else:
        result = "Invalid operator"

    # OUTPUT: Display the result to the user.
    print(f"{num1} {operator} {num2} = {result}") # formatted string

# This conditional ensures the 'main()' function is called when the script is executed directly.
if __name__ == "__main__":
    main()

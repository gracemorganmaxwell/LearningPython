# Documentation for Q1. Expression Validation

**Assignment:** IT6033 - Assignment 1
**Task:** Expression Validation
**Student:** 20200261, G Morgan-Maxwell
**Date:** November 2023
**Course:** Bachelor's Degree in Software Engineering at Whitecliffes College

## Purpose

The purpose of this program is to determine whether the user-provided expression has the correct matching bracket pairing or not.

This program is a working example of the Last-In-First-Out (LIFO) principle using a stack, which is a linear data structure. A stack allows two primary operations:

- **Push:** Adding an element to the top of the stack.
- **Pop:** Removing the top element from the stack.

## How It Works

### Expression and Bracket Characters Input

The user is prompted to enter an expression (a string) and a pair of opening and closing bracket characters (e.g., { and }).

### ExpValidator Function

The `ExpValidator` function takes three arguments: `expression`, `opening_char`, and `closing_char`. It initializes an empty stack to keep track of opening brackets.

### Loop Through Expression

The function iterates through each character in the input expression:
- If the character is an opening bracket (matches `opening_char`), it's pushed onto the stack.
- If the character is a closing bracket (matches `closing_char`), it checks the stack:
  - If the stack is empty, there is a closing bracket without a matching opening bracket, and the expression is marked as "incorrect."
  - If there's a matching opening bracket on the stack, it's popped off the stack.

### Checking for Correct Pairing

The code checks for correct bracket pairing as it goes through the expression. Whenever a closing bracket is encountered, it checks if there's a matching opening bracket on the stack. If not, the expression is marked as "incorrect."

### Final Validation

After processing the entire expression, the code checks the state of the stack:
- If the stack is empty, it means all opening brackets had matching closing brackets, and the expression is marked as "correct."
- If the stack is not empty, it means some brackets were not closed properly, or there are extra opening brackets without matching closing brackets, and the expression is marked as "incorrect."

### Result Reporting

Depending on the final state, the function returns either "correct" or "incorrect."

### User Interaction in Main Function

In the main function, the user is continuously prompted to input expressions and bracket characters. The `ExpValidator` function is called to validate each expression. The result of the validation is displayed to the user as "Valid Expression" or "Invalid Expression."

### Looping and Exiting

The program allows the user to try again or exit by responding to the "Do you want to try again? (Y/N)" prompt. If the user chooses to exit, the program displays "Bye Bye!!" and terminates.

## Summary

In summary, the code uses a stack data structure to keep track of opening brackets as it iterates through the expression. It checks for correct pairing by ensuring that each closing bracket has a matching opening bracket on the stack. After processing the entire expression, the stack's state determines whether the expression is "correct" (all brackets paired correctly) or "incorrect" (mismatched or unclosed brackets). The code then reports the result to the user and allows for further interactions.

---

Thank you for reading. This documentation provides insight into the program's purpose and operation, aiding in understanding the mechanics of its logic.

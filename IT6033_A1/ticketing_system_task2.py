"""
Assignment: IT6033 - Assignment 1
Task 2: Ticketing System Simulation
Student: 20200261, G Morgan-Maxwell
Accompaniment documentation in file: task2ReadMe.md
"""
import threading
from collections import deque
# Initialize the customer queue using deque for efficient queue operations.
customerQueue = deque()

# This global counter will uniquely identify each customer.
customerCounter = 0


def NewCustomers():
    # Declare the use of the global customer_counter to ensure it's not localized.
    global customerCounter

    # Increment the global customer counter to assign a unique number to the new customer.
    customerCounter += 1

    # Add the new customer to the queue.
    customerQueue.append(f"Customer {customerCounter}")

    # Print to the console to indicate a new customer has arrived.
    print(f"New Customer Arrived: Customer {customerCounter}")
    """
    Using threading.Timer to wait 3 seconds before calling this function again. 
    Which sets up a recurring loop, with a new customer arriving every 3 seconds.
    """
    threading.Timer(3, NewCustomers).start()


def SeeCustomers():
    # Check the queue for any waiting customers.
    if customerQueue:
        # Pop the first customer from the queue to be seen.
        customer = customerQueue.popleft()

        # Output to console that the customer is being seen.
        print(f"Customer being seen: {customer}")
    else:
        # Notify via console that there are no customers waiting.
        print("No customers to see.")
        # Schedule the SeeCustomers function to check again after 5 seconds.
        threading.Timer(5, SeeCustomers).start()


# Before starting, output a welcome message to the console before starting the service loops for the shop.

print("Welcome to our shop counter, please take a ticket and we will call your number shortly, thank you")

# Initialize the customer service process by calling NewCustomers and SeeCustomers.
NewCustomers()
SeeCustomers()

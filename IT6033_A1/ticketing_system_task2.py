import threading
from collections import deque

# Initialize a deque for the customer queue. A deque is chosen because it's optimized for
# both appending and popping from the ends, which is exactly what we need for a queue system.
customer_queue = deque()

# This global counter will uniquely identify each customer.
customer_counter = 0


def NewCustomers():
    # We need to tell Python that we'll be using the global variable 'customer_counter'
    # inside this function to ensure we're updating the global one, not creating a local one.
    global customer_counter

    # Increment the global customer counter to assign a unique number to the new customer.
    customer_counter += 1

    # Add the new customer to the queue.
    customer_queue.append(f"Customer {customer_counter}")

    # Print to the console to indicate a new customer has arrived.
    print(f"New Customer Arrived: Customer {customer_counter}")

    # Use threading.Timer to wait 3 seconds before calling this function again.
    # This sets up a recurring loop, with a new customer arriving every 3 seconds.
    threading.Timer(3, NewCustomers).start()


def SeeCustomers():
    # Check if there are any customers in the queue.
    if customer_queue:
        # Remove (pop) the first customer from the queue.
        # The popleft() operation is quick and efficient on a deque.
        customer = customer_queue.popleft()

        # Print to the console to indicate that this customer is now being seen.
        print(f"Customer being seen: {customer}")
    else:
        # If there are no customers in the queue, inform the console.
        print("No customers to see.")

    # Set up another timer to call this function again after 5 seconds,
    # creating a loop that 'sees' a customer every 5 seconds.
    threading.Timer(5, SeeCustomers).start()


# Before starting the timed loops, print a welcome message to the console.
print("Welcome to our shop counter, please take a ticket and we will call your number shortly, thank you")

# Call the functions for the first time to start the process.
NewCustomers()
SeeCustomers()

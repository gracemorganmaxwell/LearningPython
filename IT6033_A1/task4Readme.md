**Assignment:** IT6033 - Assignment 1
**Student:** 20200261, G Morgan-Maxwell
**Date:** November 2023
**Course:** Bachelor's Degree in Software Engineering at Whitecliffes College

## Task 4: Analysis of Data Structure Scripts

### Questions to  be answered:

- 	Why did you select that specific data structure?
- 	How was that data structure suited to the task?
- 	Could another data structure be used to complete the same task? If so, how would your solution differ?

------------

## Validating Expressions Script

### Why did you select that specific data structure?

I chose the stack for its Last-In-First-Out (LIFO) characteristic, which is inherently suitable for matching pairs in expressions. Upon reflection, I could have emphasized how this feature is particularly adept at managing the nested nature of valid expressions, which is a critical aspect of the task at hand.

### How was that data structure suited to the task?

The stack was well-suited because it allowed for efficient tracking of the most recent unmatched opening bracket, ensuring that each closing bracket corresponds to the correct opening bracket. In reviewing this choice, it's clear that a stack permits an *O*(n) time complexity for validation, which is optimal. However, I might have explored in greater depth the nuances of how the stack supports this process compared to other data structures that could potentially lead to increased complexity or reduced readability.

### Could another data structure be used to complete the same task? If so, how would your solution differ?

While a stack is the most straightforward data structure for this task, alternatives like a deque or a recursive function could technically accomplish the same goal. The deque, although it offers additional operations that are unnecessary for this task, would not alter the solution much since the essential stack operations are the same. A recursive solution would implicitly use the call stack but may not be as clear in its logic and could risk stack overflow errors for long expressions. Upon revisiting my solution, I see the merit in sticking to the stack for its simplicity and directness, although I'd ensure my implementation is robust against various edge cases and user input errors.


------------

## Ticketing System Script

### Why did you select that specific data structure?

I selected the deque because I recognized its performance benefits for queue operations over other data structures available in Python. It seemed the most appropriate given its fast O(1) append and pop operations from both ends. In hindsight, I might emphasize the deque's alignment with the real-world behavior of queues, which solidifies its role in the script.

### How was that data structure suited to the task?

The deque was perfectly suited to the task because it mimics the first-come-first-served nature of a physical queue. This data structure streamlined the simulation of customers arriving and being served without any unnecessary complexity. Reflecting on this, it's clear that the deque's suitability extends beyond theoretical efficiency; it offers practical benefits in readability and maintainability of the code.

### Could another data structure be used to complete the same task? If so, how would your solution differ?

While other data structures, such as lists or manually implemented linked lists, could theoretically be used to simulate a queue, they would not offer the same performance and ease of use as a deque. A list, for example, would result in less efficient pop operations from the front. If I had used a list, the solution would involve additional logic to handle the inefficiencies, potentially complicating the code. Reflecting on this, my choice of deque seems even more justified as it provides a balance between efficiency and code simplicity.

------------

## Binary Search Tree


### Why did you select that specific data structure?

I chose a binary search tree (BST) because I valued its ability to keep elements in a sorted order, which is crucial for efficient searching and insertion. This structure seemed natural for the task at hand, which involved inserting and then traversing the elements in a specific order. Looking back, I could consider self-balancing BST variants that ensure optimal performance even under varied insertions, although this would increase the complexity of the implementation.

### How was that data structure suited to the task?

The BST was well-suited because it allowed me to leverage its sorted property for quick insertions and facilitated a straightforward pre-order traversal. This traversal method is recursive by nature, which aligns well with the recursive tree structure. On reflection, it’s apparent that this choice also laid a good foundation for extending the program to perform other types of traversals if needed.

### Could another data structure be used to complete the same task? If so, how would your solution differ?

Yes, other data structures like arrays or linked lists could have been used, but they would have compromised on efficiency or simplicity. With an array, I'd have to sort the elements before traversing to maintain order, and with a linked list, I’d have to deal with more complex node management. My solution with the BST strikes a balance between efficiency and complexity. Nevertheless, I recognize that for certain datasets, particularly those with frequent insertions and deletions, a self-balancing tree or even a hash table with a linked list for handling collisions might offer better performance, albeit with a more complex codebase.
# Binary Search Tree Implementation
## Documentation for BST.py 

**Assignment:** IT6033 - Assignment 1
**Task 3:** Binary Search Tree
**Student:** 20200261, G Morgan-Maxwell
**Date:** November 2023
**Course:** Bachelor's Degree in Software Engineering at Whitecliffes College

## Purpose

The purpose of this program is to construct a binary search tree (BST) from user input and perform a pre-order traversal to display the structure of the tree.

A BST is a node-based binary tree data structure that has the following properties:

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- Both the left and right subtrees must also be binary search trees.

The program demonstrates the insertion of elements into a BST and the algorithmic process of a pre-order traversal, which visits nodes in the "root-left-right" order.

## How It Works

### Node and BST Classes

The `Node` class defines the structure of a tree node, which includes the node's data and pointers to its left and right children.

The `BST` class encapsulates the binary search tree and includes methods for inserting new data and performing pre-order traversal.

### Insertion of Elements

The user is prompted to enter a series of numbers, which will be the elements of the BST. These can be entered with or without commas (e.g., `10, 20, 30` or `10 20 30`).

The `insert` method places each new element into the correct location in the BST, preserving the BST properties.

### Pre-Order Traversal

The `pre_order_traversal` method recursively visits each node in the BST in pre-order fashion, starting from the root, then moving to the left child, and finally the right child.

### Printing the Tree

The `print_tree` method outputs the elements of the tree as they are visited during the pre-order traversal.

### Main Function and User Interaction

The `main` function handles the initialization of the BST object and user interaction. It prompts the user for input, inserts the elements into the tree, and then prints the pre-ordered list of elements.

## Example Dataset

Below is an example dataset that can be copied and pasted into the program to create a BST and see the pre-order traversal output.

50 30 70 20 40 60 80 10 25 35 45 55 65 75 85


Upon entering the above dataset, the program will output the following pre-order traversal:

50 30 20 10 25 40 35 45 70 60 55 65 80 75 85


## Summary

This BST program is a practical example of how binary search trees work, particularly highlighting how they maintain their sorted property through insertions and how data can be retrieved efficiently through traversal methods. It is a demonstration of fundamental data structures and algorithms in computer science and software engineering.

---

Thank you for reading about this BST implementation. This documentation provides insight into the program's purpose and operation, aiding in understanding the mechanics of its logic.


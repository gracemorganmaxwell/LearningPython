"""
Assignment: IT6033 - Assignment 1
Task 3: Binary Tree System
Student: 20200261, G Morgan-Maxwell
Accompaniment documentation in file: task3ReadMe.md
"""

class Node:
    # A Node has data, and potentially a left and right child.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    # The Binary Search Tree (BST) starts with a root that is None.
    def __init__(self):
        self.root = None

    # Insert function will add a node to the tree with the given data.
    def Insert(self, data):
        # If the tree is empty, the first node will become the root.
        if self.root is None:
            self.root = Node(data)
        else:
            # Otherwise, we need to find the correct place for the new node.
            self.InsertRecursive(self.root, data)

    # Recursive function to insert a new node in the correct position.
    def InsertRecursive(self, node, data):
        if data < node.data:
            # If the data is less than the current node's data, go left.
            if node.left is None:
                # If there's no left child, place the new node here.
                node.left = Node(data)
            else:
                # If there is a left child, call insert recursively on the left child.
                self.InsertRecursive(node.left, data)
        else:
            # If the data is not less than the current node's data, go right.
            if node.right is None:
                # If there's no right child, place the new node here.
                node.right = Node(data)
            else:
                # If there is a right child, call insert recursively on the right child.
                self.InsertRecursive(node.right, data)

    # Pre-order traversal: Root, Left, Right.
    def PreOrderTraversal(self, node, visited=None):
        # If this is the first call, initialize the visited list.
        if visited is None:
            visited = []
        if node:
            # Visit the root first.
            visited.append(node.data)
            # Then traverse the left subtree.
            self.PreOrderTraversal(node.left, visited)
            # Finally, traverse the right subtree
            self.PreOrderTraversal(node.right, visited)
        return visited

    # Function to print the tree using pre-order traversal.
    def PrintTree(self):
        # Get the list of visited nodes.
        visited = self.PreOrderTraversal(self.root)
        # Print the visited nodes.
        for value in visited:
            print(value, end=' ')
        print()  # New line at the end.


# Main function that will run the program.
def Main():
    # Welcome message to the user.
    print("Welcome to Gracie's Binary Search Tree (BST) program! \n This program will allow you to create a BST and "
          "perform a pre-order traversal. \n Please enter the elements you would like to add to the BST. \n You can "
          "enter the elements with or without commas. \n and for a copy/paste data"
          "set refer to my accompanying task3Readme.md file please.")

    # Take input from the user and create the tree.
    elements = input("Enter the elements to add to the BST: ").replace(',', ' ').split()
    bst = BST()
    for el in elements:
        try:
            # Insert the element into the BST after converting it to an integer.
            bst.Insert(int(el))
        except ValueError:
            # If the input cannot be converted to an integer, inform the user.
            print(f"Skipping invalid input: {el}. Please enter only integer values.")

    # Once the tree is created, print it in pre-order.
    print("\nPre-order Traversal of the BST:")
    bst.PrintTree()


if __name__ == "__main__":
    Main()

# In python lists is a collection of values that is ordered and changeable
# which lets us store multiple values in a single variable
# Initial empty to-do list
tasks = []

def display_tasks():
    """Display all the tasks in the to-do list."""
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return

    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

def add_task():
    """Add a new task to the to-do list."""
    new_task = input("Enter the new task: ").strip()  # .strip() removes any leading/trailing whitespace
    if new_task:  # check if the task is not empty
        tasks.append(new_task)
        print(f"'{new_task}' has been added to your to-do list.\n")

def remove_task():
    """Remove an existing task from the to-do list."""
    display_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)  # -1 because lists are 0-indexed
            print(f"'{removed_task}' has been removed from your to-do list.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    """Main function to manage the to-do list."""
    while True:
        print("To-Do List Manager")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()

from __future__ import annotations

from datetime import date

from db import add_task
from db import create_tables
from db import delete_task
from db import mark_task_complete
from db import quit_program
from db import view_tasks


# Main menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")


# User Input
def add_task_from_user_input():
    title = input("Enter task title: ")

    while True:
        due_date_str = input("Enter due date (YYYY-MM-DD) ")
        try:
            due_date = date.fromisoformat(due_date_str)
            if due_date < date.today():
                print(
                    """
                      Due date cannot be in the past.
                      Please enter a valid date.
                      """
                )
                continue
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

    add_task(title, due_date=due_date)


# Displays task and status to user
def print_tasks():
    tasks = view_tasks()
    for task in tasks:
        print(f"{task.id}. {task.title} - {task.completed}")


# Prompt user for task completion
def complete_task_prompt():
    view_tasks()
    task_id = int(input("Enter the number of the tasks to mark complete: "))
    mark_task_complete(task_id)


# Prompt user for task deletion
def delete_task_prompt():
    view_tasks()
    task_id = int(input("Enter the number of the task to delete: "))
    delete_task(task_id)


# Main function to handle user input
def main():
    create_tables()

    actions = {
        "1": add_task_from_user_input,
        "2": print_tasks,
        "3": complete_task_prompt,
        "4": delete_task_prompt,
        "5": quit_program,
    }

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

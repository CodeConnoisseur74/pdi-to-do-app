from __future__ import annotations

# replaced with database
tasks = []


# Main menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")


# Add tasks to list
def add_task():
    task = input("Enter a task: ")
    tasks.append(
        {"task": task, "completed": False}
    )  # new function to add to database(task)
    print("Task added!")


# View available tasks
def view_tasks():
    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index + 1}. {task['task']} - {status}")


# Mark tasks as complete
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked complete!")
    else:
        print("Invalid task number.")


# Delete tasks
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted!")
    else:
        print("Invalid task number.")


# Prompt user for task completion
def complete_task_prompt():
    view_tasks()
    index = int(input("Enter the number of the tasks to mark complete: ")) - 1
    complete_task(index)


# Prompt user for task deletion
def delete_task_prompt():
    view_tasks()
    index = int(input("Enter the number of the task to delete: ")) - 1
    delete_task(index)


# Quit the program
def quit_program():
    print("Thank you for using the To-Do List!")
    exit()


# Main function to handle user input
def main():
    actions = {
        "1": add_task,
        "2": view_tasks,
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

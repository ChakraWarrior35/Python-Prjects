task = []

def display_tasks():
    if not task:
        print("No tasks Added")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(task, 1):
            print(f"{i}. {t['name']} [{t['status']}]")

def add_task():
    new_task = input("Add your task: ")
    task.append({"name": new_task, "status": "Pending"})
    print(f'Task "{new_task}" added successfully.')

def remove_task():
    display_tasks()
    try:
        task_num = int(input("Enter the task number you want to remove: "))
        if 1 <= task_num <= len(task):
            removed_task = task.pop(task_num - 1)
            print(f'Task "{removed_task["name"]}" removed successfully.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task():
    display_tasks()
    try:
        task_num = int(input("Enter the task number you want to update: "))
        if 1 <= task_num <= len(task):
            new_task = input("Enter the new task name: ")
            task[task_num - 1]["name"] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def status_task():
    display_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(task):
            task[task_num - 1]["status"] = "Completed"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. update Task Status")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            status_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            remove_task()
        elif choice == '6':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()

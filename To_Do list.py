import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, status VARCHAR(20) NOT NULL)")
conn.commit()

def display_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]} [{task[2]}]")

def add_task():
    name = input("Enter task name: ")
    cursor.execute(
        "INSERT INTO tasks (name, status) VALUES (%s, %s)",
        (name, "Pending")
    )
    conn.commit()
    print("Task added successfully.")

def update_task():
    display_tasks()
    try:
        task_id = int(input("Enter task ID to update: "))
        new_name = input("Enter new task name: ")
        cursor.execute(
            "UPDATE tasks SET name=%s WHERE id=%s",
            (new_name, task_id)
        )
        conn.commit()
        print("Task updated successfully.")
    except ValueError:
        print("Invalid input.")

def mark_completed():
    display_tasks()
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
        cursor.execute(
            "UPDATE tasks SET status=%s WHERE id=%s",
            ("Completed", task_id)
        )
        conn.commit()
        print("Task marked as completed.")
    except ValueError:
        print("Invalid input.")

def remove_task():
    display_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
        conn.commit()
        print("Task deleted successfully.")
    except ValueError:
        print("Invalid input.")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            update_task()
        elif choice == "5":
            remove_task()
        elif choice == "6":
            print("Exiting application.")
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

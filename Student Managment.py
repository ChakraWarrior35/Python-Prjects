import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("Host"),
    user=os.getenv("User"),
    password=os.getenv("Password"),
    database=os.getenv("Database")
)

cursor = mydb.cursor()


class StudentManagement:

    def add_student(self, name, age, course, marks):
        try:
            cursor.execute(
                "INSERT INTO Students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
                (name, age, course, marks)
            )
            mydb.commit()
            print(f'Student "{name}" added successfully.')
        except mysql.connector.Error:
            print("Student already exists.")

    def update_marks(self, name, marks):
        cursor.execute(
            "UPDATE Students SET marks=%s WHERE name=%s",
            (marks, name)
        )
        mydb.commit()
        print(f'Marks updated for "{name}".')

    def delete_student(self, name):
        cursor.execute(
            "DELETE FROM Students WHERE name=%s",
            (name,)
        )
        mydb.commit()
        print(f'🗑 Student "{name}" deleted.')

    def view_students(self):
        cursor.execute(
            "SELECT * FROM Students"
        )
        records = cursor.fetchall()

        print("\nID | Name | Age | Course | Marks")
        print("-" * 40)
        for r in records:
            print(r)

    def search_student(self, name):
        cursor.execute(
            "SELECT * FROM Students WHERE name=%s",
            (name,)
        )
        student = cursor.fetchone()

        if student:
            print("\nStudent Found:")
            print(student)
        else:
            print("No student found.")


def main():
    sms = StudentManagement()

    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            sms.add_student(
                input("Name: "),
                int(input("Age: ")),
                input("Course: "),
                float(input("Marks: "))
            )
        elif choice == "2":
            sms.update_marks(
                input("Student Name: "),
                float(input("New Marks: "))
            )
        elif choice == "3":
            sms.delete_student(
                input("Student Name: ")
            )
        elif choice == "4":
            sms.view_students()
        elif choice == "5":
            sms.search_student(
                input("Student Name: ")
            )
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
    cursor.close()
    mydb.close()

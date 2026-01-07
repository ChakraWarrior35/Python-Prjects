import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = mydb.cursor()


class Library:

    def add_book(self, title):
        try:
            cursor.execute(
                "INSERT INTO Books (title) VALUES (%s)",
                (title,)
            )
            mydb.commit()
            print(f'Book "{title}" added.')
        except mysql.connector.Error:
            print("Book already exists.")

    def register_member(self, name):
        try:
            cursor.execute(
                "INSERT INTO Members (name) VALUES (%s)",
                (name,)
            )
            mydb.commit()
            print(f'Member "{name}" registered.')
        except mysql.connector.Error:
            print("Member already exists.")

    def borrow_book(self, title, member_name):
        cursor.execute(
            "SELECT id FROM Books WHERE title=%s AND is_available=TRUE",
            (title,)
        )
        book = cursor.fetchone()

        cursor.execute(
            "SELECT id FROM Members WHERE name=%s",
            (member_name,)
        )
        member = cursor.fetchone()

        if not book:
            print("Book not available.")
            return
        if not member:
            print("Member not registered.")
            return

        cursor.execute(
            "INSERT INTO BorrowedBooks (book_id, member_id) VALUES (%s, %s)",
            (book[0], member[0])
        )
        cursor.execute(
            "UPDATE Books SET is_available=FALSE WHERE id=%s",
            (book[0],)
        )
        mydb.commit()
        print(f'{member_name} borrowed "{title}".')

    def return_book(self, title):
        cursor.execute(
            """
            SELECT BorrowedBooks.id, Books.id
            FROM BorrowedBooks
            JOIN Books ON BorrowedBooks.book_id = Books.id
            WHERE Books.title=%s
            """,
            (title,)
        )
        result = cursor.fetchone()

        if not result:
            print("Book not borrowed.")
            return

        borrow_id, book_id = result

        cursor.execute(
            "DELETE FROM BorrowedBooks WHERE id=%s",
            (borrow_id,)
        )
        cursor.execute(
            "UPDATE Books SET is_available=TRUE WHERE id=%s",
            (book_id,)
        )
        mydb.commit()
        print(f'Book "{title}" returned.')

    def display_available_books(self):
        cursor.execute(
            "SELECT title FROM Books WHERE is_available=TRUE"
        )
        books = cursor.fetchall()
        print("\nAvailable Books:")
        for book in books:
            print("-", book[0])

    def display_borrowed_books(self):
        cursor.execute(
            """
            SELECT Books.title, Members.name
            FROM BorrowedBooks
            JOIN Books ON BorrowedBooks.book_id = Books.id
            JOIN Members ON BorrowedBooks.member_id = Members.id
            """
        )
        records = cursor.fetchall()
        print("\nBorrowed Books:")
        for book, member in records:
            print(f'- "{book}" borrowed by {member}')


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Available Books")
        print("6. Show Borrowed Books")
        print("7. Exit")

        choice = input("Choose (1-7): ")

        if choice == "1":
            library.add_book(input("Book title: "))
        elif choice == "2":
            library.register_member(input("Member name: "))
        elif choice == "3":
            library.borrow_book(
                input("Book title: "),
                input("Member name: ")
            )
        elif choice == "4":
            library.return_book(input("Book title: "))
        elif choice == "5":
            library.display_available_books()
        elif choice == "6":
            library.display_borrowed_books()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
    cursor.close()
    mydb.close()
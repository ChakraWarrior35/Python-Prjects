import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("Host"),
    user=os.getenv("User"),
    password=os.getenv("Password"),
    database=os.getenv("Database", "expenses_db")
)

cursor = mydb.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    amount DOUBLE
)
""")
mydb.commit()

def add_expense():
    name = entry_name.get()
    amount = entry_amount.get()

    if name == "" or amount == "":
        messagebox.showerror("Error", "Enter all fields")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Amount must be number")
        return

    cursor.execute(
        "INSERT INTO expenses (name, amount) VALUES (%s, %s)",
        (name, amount)
    )
    mydb.commit()

    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

    messagebox.showinfo("Success", "Expense Added")
    show_expenses()

def show_expenses():
    listbox.delete(0, tk.END)

    cursor.execute("SELECT name, amount FROM expenses")
    rows = cursor.fetchall()

    total = 0
    for row in rows:
        listbox.insert(tk.END, f"{row[0]} - ₹{row[1]}")
        total += float(row[1])

    label_total.config(text=f"Total Expense: ₹{total}")

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x450")

tk.Label(root, text="Expense Name").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root, width=30)
entry_amount.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

listbox = tk.Listbox(root, width=45, height=15)
listbox.pack()

label_total = tk.Label(root, text="Total Expense: ₹0")
label_total.pack(pady=10)

show_expenses()

root.mainloop()

mydb.close()

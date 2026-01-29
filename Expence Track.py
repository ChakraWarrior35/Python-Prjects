import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "expenses.txt"

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

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{amount}\n")

    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    messagebox.showinfo("Success", "Expense Added")
    show_expenses()

def show_expenses():
    listbox.delete(0, tk.END)
    total = 0

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, amount = line.strip().split(",")
                listbox.insert(tk.END, f"{name} - ₹{amount}")
                total += float(amount)

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

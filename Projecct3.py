import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) != 0:
            result = float(entry1.get()) / float(entry2.get())
        else:
            result = "Cannot divide by zero"
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter first number:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(root, font=("Helvetica", 12))
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(root, font=("Helvetica", 12))
entry2.grid(row=1, column=1, padx=10, pady=10)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.grid(row=2, columnspan=2, pady=10)

tk.Button(btn_frame, text="Add", command=add, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=10).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Subtract", command=subtract, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=10).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Multiply", command=multiply, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=10).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Divide", command=divide, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=10).grid(row=0, column=3, padx=5, pady=5)

label_result = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Helvetica", 14), width=25, anchor="w")
label_result.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()

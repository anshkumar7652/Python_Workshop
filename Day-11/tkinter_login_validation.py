import tkinter as tk
from tkinter import messagebox

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Sample credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Login Page", font=("Arial", 16))
title_label.pack(pady=10)

# Username
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password
password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Run application
root.mainloop()
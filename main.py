# SIA 2 Lab - Mini Project: Login and Registration System
import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib


# 1. setup  SQLite database and table for  users
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


# 2. Function to hash  password using  hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


class MiniProjectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SIA2  Project - Login & Register")
        self.root.geometry("350x300")

        init_db()
        self.build_login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_login_screen(self):
        self.clear_window()

        tk.Label(self.root, text=" Login", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.user_entry = tk.Entry(self.root, width=25)
        self.user_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()
        self.pass_entry = tk.Entry(self.root, show="*", width=25)
        self.pass_entry.pack(pady=5)

        tk.Button(self.root, text="Login", width=15, command=self.handle_login).pack(pady=5)

        tk.Button(self.root, text="Register ", width=18, command=self.build_register_screen).pack(pady=5)

    def build_register_screen(self):
        self.clear_window()

        tk.Label(self.root, text="User Registration", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Choose Username:").pack()
        self.reg_user_entry = tk.Entry(self.root, width=25)
        self.reg_user_entry.pack(pady=5)

        tk.Label(self.root, text="Choose Password:").pack()
        self.reg_pass_entry = tk.Entry(self.root, show="*", width=25)
        self.reg_pass_entry.pack(pady=5)

        # to save in SQLite database
        tk.Button(self.root, text="Sign Up", width=15, command=self.save_user).pack(pady=10)
        tk.Button(self.root, text="Back to Login", width=15, command=self.build_login_screen).pack()

    def save_user(self):
        username = self.reg_user_entry.get()
        password = self.reg_pass_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields must be filled out!")
            return

        secure_password = hash_password(password)

        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, secure_password))
            conn.commit()
            conn.close()

            messagebox.SUCCESS = messagebox.showinfo("Success", "Account registered successfully!")
            self.build_login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "That username is already taken! Please choose another one.")

    def handle_login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "Enter the username and password!")
            return

        secure_password = hash_password(password)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, secure_password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Welcome", f"Login successful!, {username}!")
        else:
            messagebox.showerror("Failed", "Wrong username or password.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniProjectApp(root)
    root.mainloop()

# main lanch window for GUI

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

users = {}

def register_user(username, password):
    if username in users:
        print("Username already exists.")
        return False
    users[username] = password
    print("User registered successfully.")

def login_user(username, password):
    if username not in users or users[username] != password:
        print("Invalid username or password.")
        return False
    return True, "Login successful."


class ImagePage(tk.Frame):
    def __init__(self, master, image_path, on_click=None):
        super().__init__(master)
        self.on_click = on_click

        # Load and display image
        image = Image.open(image_path)
        image = image.resize((900, 600))  # adjust to window size
        self.photo = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=self.photo)
        label.pack()

        if self.on_click:
            label.bind("<Button-1>", lambda e: self.on_click())
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Password")

        tk.Button(self, text="Login", command=self.handle_login).pack(pady=5)
        tk.Button(self, text="Register", command=self.handle_register).pack(pady=5)
    def handle_login(self):
            username = self.username_entry.get()
            password = self.password_entry.get()
            success, message = login_user(username, password)
            messagebox.showinfo("Login", message)
            if success and self.on_click:
                self.on_click()  # Switch to dashboard

    def handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = register_user(username, password)
        messagebox.showinfo("Register", message)


def launch_app():
    root = tk.Tk()
    root.geometry("900x600")
    root.title("AI IDS Prototype")

    def show_dashboard():
        for widget in root.winfo_children():
            widget.destroy()
        dashboard = ImagePage(root, "gui/assets/Dashboard.png")
        dashboard.pack()
    

    login = ImagePage(root, "gui/assets/LoginPage.png", on_click=show_dashboard)
    login.pack()

    root.mainloop()

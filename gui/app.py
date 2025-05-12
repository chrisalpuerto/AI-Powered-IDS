# main lanch window for GUI

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

users = {}

from gui.gui import open_login_page
from gui.gui2 import open_dashboard_page

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

def la():
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

launch_app = open_login_page
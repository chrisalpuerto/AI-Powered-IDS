# main lanch window for GUI

import tkinter as tk
from PIL import Image, ImageTk

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

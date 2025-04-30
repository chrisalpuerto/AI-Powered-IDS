# main lanch window for GUI

import tkinter as tk
from gui.dashboard import Dashboard

def launch_gui():
    root = tk.Tk()
    root.title("AI-Powered IDS")
    root.geometry("900x600")

    # Create a Dashboard instance
    app = Dashboard(root)
    app.pack(fill=tk.BOTH, expand=True)

    # Start the main loop
    root.mainloop()
# dashboard

import tkinter as tk
from tkinter import ttk

class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.log_box = tk.Text(self, height=20, width=80)
        self.log_box.pack(pady=10)

        self.start_button = tk.Button(self, text="Start IDS", command=self.start_ids)
        self.start_button.pack()

    def start_ids(self):
        self.log_box.insert(tk.END, "Starting intrusion detection...\n")
        # call model here to classify incoming packets

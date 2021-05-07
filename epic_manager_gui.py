import tkinter as tk
from epic_manager import EpicManager

class EpicManagerGui:
    def __init__(self):
        self.epic_id = ""
        self.main_window = None
        self.epic_label = None
        self.epic_text = None
        self.manage_button = None
        self.epic_manager = EpicManager()

    def show(self):
        self.main_window = tk.Tk()
        self.main_window.title("Epic Manager")
        self.main_window.geometry("300x100")
        self.epic_label = tk.Label(self.main_window, text="Epic ID:")
        self.epic_text = tk.Entry(self.main_window, width=25)
        self.manage_button = tk.Button(self.main_window, text="Manage Epic")
        self.epic_label.grid(column=0, row=0)
        self.epic_text.grid(column=1, row=0)
        self.manage_button.grid(column=1, row=2)
        self.manage_button.bind("<Button-1>", self.manage_epic)
        self.main_window.mainloop()

    def manage_epic(self, event):
        epic_id = self.epic_text.get()
        if epic_id != "":
            self.epic_manager.manage_epic(epic_id)

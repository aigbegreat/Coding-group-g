import tkinter as tk

class BankApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Bank App")

        self.balance = 0

        self.create_widgets()

    def create_widgets(self):
        self.balance_label = tk.Label(self.master, text="Balance: $0")
        self.balance_label.pack()


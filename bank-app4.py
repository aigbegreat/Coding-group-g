def deposit(self):
    amount = float(self.amount_entry.get())
    self.balance += amount
    self.update_balance()


def withdraw(self):
    amount = float(self.amount_entry.get())
    if amount <= self.balance:
        self.balance -= amount
        self.update_balance()
    else:
        tk.messagebox.showerror("Error", "Insufficient funds")
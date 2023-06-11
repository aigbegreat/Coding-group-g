self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
self.deposit_button.pack()

# Create a button for withdrawing money
self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw)
self.withdraw_button.pack()


def select_savings(self):
    self.account_label.config(text="Account Type: Savings")


def select_current(self):
    self.account_label.config(text="Account Type: Current")

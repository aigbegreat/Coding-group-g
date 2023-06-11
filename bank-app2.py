self.account_label = tk.Label(self.master, text="Account Type: None")
self.account_label.pack()

# Create a button for selecting savings account
self.savings_button = tk.Button(self.master, text="Savings Account", command=self.select_savings)
self.savings_button.pack()

# Create a button for selecting current account
self.current_button = tk.Button(self.master, text="Current Account", command=self.select_current)
self.current_button.pack()

# Create an entry for depositing/withdrawing money
self.amount_entry = tk.Entry(self.master)
self.amount_entry.pack()



 def update_balance(self):
        self.balance_label.config(text="Balance: ${:.2f}".format(self.balance))

if __name__ == "__main__":
    root = tk.Tk()
    bank_app =BankApp(root)
    root.mainloop()
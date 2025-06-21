import os

class BankAccount:
    def __init__(self, balance_file="balance.txt"):
        self.balance_file = os.path.join(os.path.dirname(__file__), balance_file)
        self.account_balance = self._load_balance()

    def _load_balance(self):
        if os.path.exists(self.balance_file):
            with open(self.balance_file, "r") as file:
                try:
                    return float(file.read())
                except ValueError:
                    return 0.0
        return 0.0

    def save_balance(self):
        with open(self.balance_file, "w") as file:
            file.write(f"{self.account_balance:.2f}")

    def deposit(self, amount):
        self.account_balance += amount
        self.save_balance()
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            self.save_balance()
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

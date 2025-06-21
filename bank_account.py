import os

class BankAccount:
    def __init__(self, balance_file="balance.txt"):
        self.balance_file = os.path.join(os.path.dirname(__file__), balance_file)
        if not os.path.exists(self.balance_file):
            with open(self.balance_file, "w") as f:
                f.write("0.0")

    def _read_balance(self):
        with open(self.balance_file, "r") as f:
            return float(f.read().strip())

    def _write_balance(self, amount):
        with open(self.balance_file, "w") as f:
            f.write(f"{amount:.2f}")

    def deposit(self, amount):
        balance = self._read_balance()
        balance += amount
        self._write_balance(balance)
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        balance = self._read_balance()
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            self._write_balance(balance)
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        balance = self._read_balance()
        print(f"Current Balance: ${balance:.2f}")
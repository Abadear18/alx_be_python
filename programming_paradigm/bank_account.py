class BankAccount:
    def __init__(self):
        self.account_balance = 0.0

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
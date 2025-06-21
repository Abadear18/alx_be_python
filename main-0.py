from bank_account import BankAccount
import sys

def main():
    account = BankAccount(initial_balance=250)

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command.startswith("deposit:"):
            amount = float(command.split(":")[1])
            account.deposit(amount)
        elif command.startswith("withdraw:"):
            amount = float(command.split(":")[1])
            account.withdraw(amount)
        elif command == "display":
            account.display_balance()

if __name__ == "__main__":
    main()
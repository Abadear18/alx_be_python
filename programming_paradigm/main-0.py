from bank_account import BankAccount
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        return

    command = sys.argv[1]
    account = BankAccount()

    if command.startswith("deposit:"):
        try:
            amount = float(command.split(":")[1])
            account.deposit(amount)
        except ValueError:
            print("Invalid deposit amount.")
    elif command.startswith("withdraw:"):
        try:
            amount = float(command.split(":")[1])
            account.withdraw(amount)
        except ValueError:
            print("Invalid withdraw amount.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount> or display")
        return

    command = sys.argv[1]

    if command.startswith("deposit:"):
        amount = float(command.split(":")[1])
        account.deposit(amount)
    elif command.startswith("withdraw:"):
        amount = float(command.split(":")[1])
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
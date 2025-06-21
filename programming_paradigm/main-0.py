import sys
from bank_account import BankAccount

account = BankAccount()

commands = sys.argv[1:]

for command_input in commands:
    if ':' in command_input:
        command, amount = command_input.split(':')
        amount = float(amount)
    else:
        command = command_input
        amount = None

    if command == "deposit":
        account.deposit(amount)
    elif command == "withdraw":
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use deposit, withdraw, or display.")
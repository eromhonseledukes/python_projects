#updated

class Account:
    def __init__(self, customer_name, bank_name, account_number, initial_balance=0.0):
        self.customer_name = customer_name
        self.bank_name = bank_name
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount
        print(f"Deposited {amount}. Current balance: {self.initial_balance}")

    def withdraw(self, amount):
        if amount <= self.initial_balance:
            self.initial_balance -= amount
            print(f"Withdrawn {amount}. Current balance: {self.initial_balance}")
        else:
            print("Insufficient Funds")

    def check_balance(self):
        print(f"Current balance: {self.initial_balance}")

    def transfer_funds(self, recipient_account, amount):
        if amount <= self.initial_balance:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            print(f"Transferred {amount} from {self.customer_name} at {self.bank_name} to {recipient_account.customer_name} at {recipient_account.bank_name}.")
        else:
            print("Insufficient Funds for transfer")

    def display_info(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Initial Balance: {self.initial_balance}")

customer_name = input("Enter your name: ")
bank_name = input("Enter your bank name: ")
account_number = int(input("Enter your account number: "))
initial_deposit = float(input("Enter initial deposit amount: "))

account1 = Account(customer_name, bank_name, account_number, initial_deposit)

print("\nCustomer Information:")
account1.display_info()

deposit_amount = float(input("Enter amount to deposit: "))
account1.deposit(deposit_amount)

withdrawal_amount = float(input("Enter amount to withdraw: "))
account1.withdraw(withdrawal_amount)

recipient_bank_name = input("Enter recipient bank name: ")
recipient_account_number = int(input("Enter recipient account number: "))
recipient_customer_name = input("Enter recipient customer name: ")
transfer_amount = float(input("Enter amount to transfer: "))

recipient_account = Account(recipient_customer_name, recipient_bank_name, recipient_account_number)

account1.transfer_funds(recipient_account, transfer_amount)

print("\nUpdated Account Information:")
account1.display_info()

print("\nSender's balance and details:")
print(f"Sender Name: {account1.customer_name}")
print(f"Sender Account Number: {account1.account_number}")
print(f"Sender Bank Name: {account1.bank_name}")

print("\nRecipient's balance and details:")
recipient_account.check_balance()
print(f"Recipient Name: {recipient_account.customer_name}")
print(f"Recipient Account Number: {recipient_account.account_number}")
print(f"Recipient Bank Name: {recipient_account.bank_name}")

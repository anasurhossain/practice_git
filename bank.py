class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposit: ${amount}. The new balance is: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: ${amount}. The new balance is: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        print(f"Final balance: {self.balance}")
# Test case 1
account = BankAccount("John Doe", 100.0)
account.deposit(50.0)
account.withdraw(30.0)
account.get_balance()

# Test case 2
account = BankAccount("John Doe", 10.0)
account.deposit(-50.0)
account.withdraw(30.0)
account.get_balance()

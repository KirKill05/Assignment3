class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds")
            return False

    def get_balance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, min_balance=0):
        super().__init__(account_holder, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= self.balance - self.min_balance:
            self.balance -= amount
            return True
        else:
            print("Transaction rejected. Below minimum balance.")
            return False


class ChequingAccount(Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            print("Transaction rejected. Overdraft limit exceeded.")
            return False
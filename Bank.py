from Account import *

class Bank:
    def __init__(self):
        self.accounts = []
        self.initialize_accounts()

    def initialize_accounts(self):
        # Just random list of SavingsAccount type accounts
        self.accounts.append(SavingsAccount(1, "Ragatha", 5000, 1000))
        self.accounts.append(SavingsAccount(2, "Rick", 7000, 1500))
        self.accounts.append(SavingsAccount(3, "Amanda", 9000, 2000))
        # Just random list of ChequingAccount type accounts
        self.accounts.append(ChequingAccount(4, "Mandy", 1000, 5000))
        self.accounts.append(ChequingAccount(5, "Jack", 2000, 3000))
        self.accounts.append(ChequingAccount(6, "Leo", 3000, 2000))    

    def searchAccount(self, _accountNumber):
        for account in self.accounts:
            if account._accountNumber == _accountNumber:
                return account
        print("Account not found.")
        return None
    
    def handle_transaction(self, account, transaction_type, amount):
        try:
            amount = float(amount)

            if amount < 0:
                raise ValueError("Transaction amount cannot be negative.")

            if transaction_type == "deposit":
                account.deposit(amount)
                print("Deposit of", amount, "CAD successful. New balance:", account.get_balance(), "CAD")
            elif transaction_type == "withdraw":
                if account.withdraw(amount):
                    print("Withdrawal of", amount, "CAD successful. New balance:", account.get_balance(), "CAD")
                else:
                    print("Withdrawal failed.")

        except ValueError as e:
            print("Error:", e)
class Account:
    def __init__(self, _accountNumber, _accountHolderName, _rateOfInterest, _currentBalance):
        self._accountNumber = _accountNumber
        self._accountHolderName = _accountHolderName
        self._rateOfInterest = _rateOfInterest
        self._currentBalance = _currentBalance

    def getAccountNumber(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def getRateOfInterest(self):
        return self._rateOfInterest
    
    def getCurrentBalance(self):
        return self._currentBalance
    
    def setAccountHolderName(self, newAccountHolderName):
        self._accountHolderName = newAccountHolderName

    def setRateOfInterest(self, newRateOfInterest):
        self._accountHolderName = newRateOfInterest

    def deposit(self, amount):
        self._currentBalance += amount

    def withdraw(self, amount):
        if amount <= self._currentBalance:
            self._currentBalance -= amount
            return True
        else:
            print("Insufficient funds")
            return False
    
class SavingsAccount(Account):
    def __init__(self, _accountHolderName, _currentBalance, _minimumBalance):
        super().__init__(_accountHolderName, _currentBalance)
        self._minimumBalance = _minimumBalance

    def withdraw(self, amount):
        if amount <= self._currentBalance - self._minimumBalance:
            self._currentBalance -= amount
            return True
        else:
            print("Transaction rejected. Below minimum balance.")
            return False


class ChequingAccount(Account):
    def __init__(self, _accountHolderName, _currentBalance, _overdraftLimit):
        super().__init__(_accountHolderName, _currentBalance)
        self._overdraftLimit = _overdraftLimit

    def withdraw(self, amount):
        if amount <= self._currentBalance + self._overdraftLimit:
            self._currentBalance -= amount
            return True
        else:
            print("Transaction rejected. Overdraft limit exceeded.")
            return False
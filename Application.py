from Bank import *
from Account import *

bank = Bank()
current_account = None

def showAccountMenu():
    while True:
        print("Welcome to Your Account, how can we help you today?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit account")
        responce = input("Type number of option you want to use!")
        if responce == 4:
            print("Thank you for using Super Bank!")
            break
        elif responce == 1:
            print("Your current balance is:", current_account.getCurrentBalance(), "CAD")
        elif responce == 2:
            amount = input("Enter the amount you want to deposit: ")
            bank.handle_transaction(current_account, "deposit", amount)
        elif responce == 3:
            amount = input("Enter the amount you want to withdraw: ")
            bank.handle_transaction(current_account, "withdraw", amount)
        else:
            print("Invalid choice. Please enter a valid option.")
        
def showMainMenu():
    while True:
        print("1. Select account")
        print("2. Exit")
        responce = input("Type number of option you want to use!")
        if responce == "1":
            acc_num = input("Please enter your account number:")
            current_account = bank.searchAccount(acc_num)
            if current_account:
                showAccountMenu()
        elif responce == "2":
            print("Thank you for using Super Bank!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
                
def run():
    print("Welcome to Super Bank!\n Choose your options:")
    showMainMenu()
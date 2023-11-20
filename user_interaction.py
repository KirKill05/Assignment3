def showAccountMenu():
    while True:
        print("Welcome to Your Account, how I can help you today?")
        print("Check Balance")
        print("Deposit")
        print("Withdraw")
        print("Exit account")
        print("Type in option you want as you see to choose it!")
        responce = input()
        if responce == "Exit Account":
            print("Thank you for using Super Bank!")
            break
        elif responce == "Check Balance":
            print("Your balance it:")
        elif responce == "Deposit":
            print("How much you want to Deposit?")
            deposit = int(input("Enter the amount:"))
        elif responce == "Withdraw":
            print("How much you want to Withdraw?")
            withdraw = int(input("Enter the amount:"))
        
def showMainMenu():
    while True:
        print("Welcome to Super Bank!\n Choose your options:")
        print("Select account")
        print("Exit")
        print("Type in option you want as you see to choose it!")
        responce = input()
        if responce == "Select account":
            print("Please enter your account number:")
            showAccountMenu()
        elif responce == "Exit":
            print("Thank you for using Super Bank!")
            break
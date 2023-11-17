class Bank():
    def showMainMenu():
        while True:
            print("Welcome to Super Bank!\n Choose your options:")
            print("Select account")
            print("Exit")
            print("Type in option you want as you see to choose it!")
            responce = input("")
            if responce == "Select account":
                print("Please enter your account number:")
            elif responce == "Exit":
                print("Thank you for using Super Bank!")
                break
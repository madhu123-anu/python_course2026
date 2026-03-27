class BankAccount:
    def __init__(self, name, acc_no, pin, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient Balance!")

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect old PIN!")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter Name: ")
        acc_no = input("Enter Account Number: ")
        pin = input("Set PIN: ")

        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = BankAccount(name, acc_no, pin, 0)
            print("Account created successfully!")

    def login(self):
        acc_no = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        if acc_no in self.accounts and self.accounts[acc_no].pin == pin:
            print(f"Welcome {self.accounts[acc_no].name}!")
            self.account_menu(self.accounts[acc_no])
        else:
            print("Invalid account or PIN!")

    def account_menu(self, account):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")

            choice = int(input("Enter choice: "))

            if choice == 1:
                account.check_balance()

            elif choice == 2:
                amt = int(input("Enter amount: "))
                account.deposit(amt)

            elif choice == 3:
                amt = int(input("Enter amount: "))
                account.withdraw(amt)

            elif choice == 4:
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                account.change_pin(old_pin, new_pin)

            elif choice == 5:
                print("Logged out successfully!")
                break

            else:
                print("Invalid choice!")

    def main_menu(self):
        while True:
            print("\n====== BANK MENU ======")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.create_account()

            elif choice == 2:
                self.login()

            elif choice == 3:
                print("Thank you for using Bank System!")
                break

            else:
                print("Invalid choice!")


# Run the system
bank = BankSystem()
bank.main_menu()
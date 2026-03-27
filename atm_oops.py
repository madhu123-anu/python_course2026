#laptop 
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}GB")
        print(f"Price: ₹{self.price}")

    def upgrade_ram(self, extra):
        self.ram += extra
        print(f"RAM upgraded to {self.ram}GB")

    def discount(self, percent):
        self.price -= (self.price * percent / 100)
        print(f"New Price after {percent}% discount: ₹{self.price}")
lap1 = Laptop("HP", 8, 50000)

lap1.display()
lap1.upgrade_ram(8)
lap1.discount(10)

#ATM
#1.single inheritance
class bank():
    def __init__(self,bank_name, acc_num,acc_hol,balance=0):
        self.acc_num=acc_num
        self.acc_hol=acc_hol
        self.balance=balance
        self.bank_name=bank_name
    
    def check_balance(self,balance=0):
        print("the balance is:",self.balance)
    def credit(self,amount):
        amount=int(input("enter your money:"))
        self.balance+=amount
        print("the balance after credit:",self.balance)
    def debit(self,amount):
        amount=int(input("enter your money:"))
        if amount<=self.balance:
            self.balance-=amount
            print(self.balance)
        else:
            print("insufficinet balance:")
       
class atm(bank):
    def machine(self):
        while True:   
            print("1.credit")
            print("2.debit")
            print("3.check_balance")
            print("4.exit")
            choice=int(input("enter your choice"))
            if choice==1:
                self.credit(5000)
            elif choice==2:
                self.debit(2000)
            elif choice==3:
                self.check_balance(0)
            else:
                print("invalid choice!")
                break

user=atm("sbi",123,"madhu",200000)
print(user.bank_name)
print(user.acc_num)
print(user.acc_hol)
print(user.balance)
user.machine()

#MULTILEVEL INHERITANCE

class bank():
    def __init__(self,bank_name, acc_num,acc_hol,balance=0):
        self.acc_num=acc_num
        self.acc_hol=acc_hol
        self.balance=balance
        self.bank_name=bank_name
    
    def check_balance(self,balance=0):
        print("the balance is:",self.balance)
    def credit(self,amount):
        amount=int(input("enter your money:"))
        self.balance+=amount
        print("the balance after credit:",self.balance)
class atm1(bank):
    def debit(self,amount):
        amount=int(input("enter your money:"))
        if amount<=self.balance:
            self.balance-=amount
            print(self.balance)
        else:
            print("insufficinet balance:")
       
class atm(atm1):
    def machine(self):
        while True:   
            print("1.credit")
            print("2.debit")
            print("3.check_balance")
            print("4.exit")
            choice=int(input("enter your choice"))
            if choice==1:
                self.credit(5000)
            elif choice==2:
                self.debit(2000)
            elif choice==3:
                self.check_balance(0)
            else:
                print("invalid choice!")
                break

user=atm("sbi",123,"madhu",200000)
print(user.bank_name)
print(user.acc_num)
print(user.acc_hol)
print(user.balance)
user.machine()

#HEIRARCHIAL INHERITANCE

class bank():
    def __init__(self,bank_name, acc_num,acc_hol,balance=0):
        self.acc_num=acc_num
        self.acc_hol=acc_hol
        self.balance=balance
        self.bank_name=bank_name
    
    def check_balance(self,balance=0):
        print("the balance is:",self.balance)
    def credit(self,amount):
        amount=int(input("enter your money:"))
        self.balance+=amount
        print("the balance after credit:",self.balance)
class atm1(bank):
    def debit(self,amount):
        amount=int(input("enter your money:"))
        if amount<=self.balance:
            self.balance-=amount
            print(self.balance)
        else:
            print("insufficinet balance:")
       
class atm(bank):
    def machine(self):
        while True:   
            print("1.credit")
            print("2.debit")
            print("3.check_balance")
            print("4.exit")
            choice=int(input("enter your choice"))
            if choice==1:
                self.credit(5000)
            elif choice==2:
                self.debit(2000)
            elif choice==3:
                self.check_balance(0)
            else:
                print("invalid choice!")
                break

user=atm("sbi",123,"madhu",200000)
print(user.bank_name)
print(user.acc_num)
print(user.acc_hol)
print(user.balance)
user.machine()

#MULTIPLE INHERITANCE
class bank():
    def __init__(self,bank_name, acc_num,acc_hol,balance=0):
        self.acc_num=acc_num
        self.acc_hol=acc_hol
        self.balance=balance
        self.bank_name=bank_name
    
    def check_balance(self,balance=0):
        print("the balance is:",self.balance)
    def credit(self,amount):
        amount=int(input("enter your money:"))
        self.balance+=amount
        print("the balance after credit:",self.balance)
class atm1():
    def debit(self,amount):
        amount=int(input("enter your money:"))
        if amount<=self.balance:
            self.balance-=amount
            print(self.balance)
        else:
            print("insufficinet balance:")
       
class atm(bank,atm1):
    def machine(self):
        while True:   
            print("1.credit")
            print("2.debit")
            print("3.check_balance")
            print("4.exit")
            choice=int(input("enter your choice"))
            if choice==1:
                self.credit(5000)
            elif choice==2:
                self.debit(2000)
            elif choice==3:
                self.check_balance(0)
            else:
                print("invalid choice!")
                break

user=atm("sbi",123,"madhu",200000)
print(user.bank_name)
print(user.acc_num)
print(user.acc_hol)
print(user.balance)
user.machine()


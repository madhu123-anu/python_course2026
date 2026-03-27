#.ATM PROGRAM USING FUNCTIONS
balance=0
def check_balance():
    global balance
    print(f"The current balance is {balance} ")
def deposit():
    global balance
    amount=int(input("enter the amount:"))
    if amount>=0:
        balance+=amount
        print(balance)
    else:
        print("invalid!")
def withdraw():
    global balance
    amount=int(input("enter the amount:"))
    if amount<=balance:
        balance-=amount
        print(balance)
    else:
        print("insufficienct balance")
def atm():
    while True:
       choice=int(input("enter your choice:"))
       print("1.check balance")
       print(f"2.deposit")
       print(f"3.withdraw")
       print(f"4.exit")
       if choice==1:
           check_balance()
       elif choice==2:
           deposit()
       elif choice==3:
           withdraw()
       else:
           print(f"Thankyou for visiting!!!!")
           break
atm()      

           
    
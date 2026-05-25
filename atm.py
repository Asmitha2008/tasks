def atm():
    print("Welcome to the ATM!")
    print("Please insert your card and enter your PIN.")
atm()
account=int(input("Please enter your account number: "))
password=input("Please enter your password: ")
total_balance=int(input("Please enter your total balance: "))
def withdraw():
    withdraw=int(input("Enter the amount you want to withdraw: "))
    if withdraw<=total_balance:
        print("You have withdrawn rupees",withdraw)
        print("Your remaining balance is",total_balance-withdraw)
    else:
        print("Insufficient balance")
withdraw()
def deposit(minimum_deposit,maximum_deposit):
    money=int(input("Enter the amount you want to deposit: "))
    if money>=minimum_deposit and money<=maximum_deposit:
        print("You have deposited rupees",money)
        print("Your remaining balance is",total_balance+money)
    else:
        print("Minimum deposit amount is",minimum_deposit)
        print("Maximum deposit amount is",maximum_deposit)
deposit(1000,10000000)
def check_balance():
    check=input("Do you want to check your money before deposit and withdraw ? (yes,no): ")
    if check=="yes":
        print("Your balance is",total_balance)
    else:
        print("Thank you for using the ATM!")
check_balance()

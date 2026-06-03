import sys
class bank:
    def bank (self):
        print("WELCOME TO BANKING SYSTEM")
        print("================================")
        print("HDFC BANK")
        print("================================")   
class id(bank):
    def id(self):
        idcard=input("What is your id card (aadhar card/pan card/driving license):  ")
        acc_number=int(input("Enter your account number: "))
        if idcard=="aadhar card" or idcard=="pan card" or idcard=="driving license":
            print("id card is correct")
            if acc_number==123 or acc_number==456 or acc_number==789:
                print("account number is correct")
            else:
                print("account number is wrong")
                sys.exit()
        else:
            print("id card is wrong")  
            sys.exit()
class amt(id):
    def amount(self):
        amount=int(input("Enter the amount in your account: "))
        deposit=int(input("Enter the amount you want to deposit: "))
        if deposit<1000:
            print("   MINIMUM DEPOSIT AMOUNT IS 1000")
            print("   you have deposited rupees",deposit)
        elif deposit>=1000 and deposit<500000:
            print("   YOU HAVE SUFFICIENT BALANCE IN YOUR ACCOUNT")
            print("   you have deposited rupees",deposit)
        elif deposit>=500000:
            print("   HURRAY!HIGH SAVINGS IN YOUR ACCOUNT")
            print("   you have deposited rupees",deposit)
        withdraw=int(input("Enter the amount you want to withdraw: "))
        if withdraw<amount:
            print("   You have withdrawn rupees",withdraw)
            print("   Your remaining balance is",amount-withdraw+deposit)
            if withdraw<=500000:
                print("   Your withdrawal amount is within the limit")
                print(" Withdrawal successful")
            else:
                print("   Your withdrawal amount exceeds the limit")
                print(" Withdrawal unsuccessful")
                sys.exit()
        else:
            print("   Insufficient balance")
            sys.exit()
class amt_slip(amt):
    def amt_slip(self):
        #slip details
        print("slip details")
        name=input("Enter your name: ")
        acc_no=int(input("Enter your account number: "))
        phno=int(input("Enter your phone number: "))
        date=input("Enter the date of transaction: ")
        total_amount=int(input("Enter the final balance in your account: "))
        print("    Name: ",name)
        print("    Account number: ",acc_no)
        print("    Phone number: ",phno)
        print("    Date of transaction: ",date)
        print("    Total amount in your account: ",total_amount) 
a=amt_slip()
a.bank()
a.id()
a.amount()
a.amt_slip()
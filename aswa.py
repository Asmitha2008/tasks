class bank:
    def bank (self):
        print("WELCOME TO  online BANKING SYSTEM")
        print("*******************************")
        print("canara BANK")
        print("*******************************")
class id(bank):
    def id(self):
        idcard=input("enter your user name:  ")
        password=input("enter your password:  ")
        while idcard!="aswa" or password!="1212":
            print("invalid username or password")
            idcard=input("enter your user name:  ")
            password=input("enter your password:  ")
        print("username and password are correct")
            
        
class ph(id):
    def ph(self):
        n=int(input('enter ph no: '))
        while n!=1234567890:
            print("invalid ph no")
            n=int(input('enter ph no: '))
class amt_slip(ph):
    def amt_slip(self):
        otp=int(input("enter the otp: "))
        while otp!=1234:
            print("invalid otp")
            otp=int(input("enter the otp: "))
class main(amt_slip):
    def main(self):
        print("you have successfully logged in to your account")
        print("you can now access your account details and perform transactions")
        debit=int(input("enter the amount you want to credit: "))
        withdraw=int(input("enter the amount you want to withdraw: "))
        total_amount=100000
        balance_withdraw=total_amount-withdraw
        balance=total_amount+debit-withdraw
        print("your debited amount is rs.",debit)
        print("your withdrawn amount is rs.",balance_withdraw)
        print("your total balance is rs.",balance)


m=bank()
m.bank()
n=id()
n.id()
p=ph()
p.ph()
s=amt_slip()
s.amt_slip()
a=main()
a.main()
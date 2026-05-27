class bank:
    def bank_name(self):
       print("WELCOME TO BANKING SYSTEM")
       print("PLEASE INSERT YOUR CARD AND ENTER THE PIN")
       print("      PLEASE PLACE YOUR CARD INSERTED DURING THE TRANSACTION ")
       n="123"
       re_type=""
       while re_type !=n:
        re_type=input("Enter the pin: ")
        if re_type!=n:
            print('Your pin wrong enter thee right one')
        else:
            print("access granted")
class amt(bank):
    def amount(self):
        totalamount=100000
        amount=input("do u want to withdraw (yes/no)")
        if amount=="yes":
            p=int(input('ENTER THE AMOUNT YOU WANT TO WITHDRAW'))
            balance=totalamount-p
            print('your withdrawal amount is rs.',p)
            print('your balance is',balance)
        else:
            print('REMAINING BALANCE IN YouR ACCOUNT',totalamount)
a=amt()
a.bank_name()
a.amount()
        
       
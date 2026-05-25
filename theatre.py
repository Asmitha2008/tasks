seat=1
while seat<=18:
    amount=int(input("Enter the amount: "))
    if amount>=200:
        print("seat booked @",seat)
        seat+=1
    else:
        print("insufficient amount, please pay 200 or more")

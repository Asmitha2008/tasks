#while loop library management
book_1="     Akbar Birbal"
book_2="     Panchatantra"
book_3="     Ramayana"
book_4="     Mahabharata"
book_5="     Why the constitution was made"
books=[book_1, book_2, book_3, book_4, book_5]
print("Welcome to the library management system")
print("Available books:")
for a in books:
    print(a)
book=5
while book>=1:
    member=input("Are you a member of the library? (yes/no): ")
    if member=="yes":
        print("You are a member of the library. You can borrow books.")
    else:
        print("You are not a member of the library. You cannot borrow books.")
        break
    book=int(input("Enter the number of the book you want to borrow (1-5): "))
    if book==1:
        print("You have borrowed Akbar Birbal")
        print("Please return the book within 14 days.")
        print("if you return the book late, you will be charged a fine of Rs. 5 per day.")
        print("Recipt")
        name=input("Enter your name: ")
        location=input("Enter your location: ")
        date=input("Enter the date of issue: ")
        phno=input("Enter your phone number: ")
        print("your recipt is ready,keep it safe.") 
        break
    elif book==2:
        print("You have borrowed Panchatantra")
        print("Please return the book within 14 days.")
        print("if you return the book late, you will be charged a fine of Rs. 5 per day.")
        print("Recipt")
        name=input("Enter your name: ")
        location=input("Enter your location: ")
        date=input("Enter the date of issue: ")
        phno=input("Enter your phone number: ")
        print("your recipt is ready,keep it safe.")
        break
    elif book==3:
        print("You have borrowed Ramayana")
        print("Please return the book within 14 days.")
        print("if you return the book late, you will be charged a fine of Rs. 5 per day.")
        print("Recipt")
        name=input("Enter your name: ")
        location=input("Enter your location: ")
        date=input("Enter the date of issue: ")
        phno=input("Enter your phone number: ")
        print("your recipt is ready,keep it safe.")
        break
    elif book==4:
        print("You have borrowed Mahabharata")
        print("Please return the book within 14 days.")
        print("if you return the book late, you will be charged a fine of Rs. 5 per day.")
        print("Recipt")
        name=input("Enter your name: ")
        location=input("Enter your location: ")
        date=input("Enter the date of issue: ")
        phno=input("Enter your phone number: ")
        print("your recipt is ready,keep it safe.")
        break
    elif book==5:
        print("You have borrowed Why the constitution was made")
        print("Please return the book within 14 days.")
        print("if you return the book late, you will be charged a fine of Rs. 5 per day.")
        print("Recipt")
        name=input("Enter your name: ")
        location=input("Enter your location: ")
        date=input("Enter the date of issue: ")
        phno=input("Enter your phone number: ")
        print("your recipt is ready,keep it safe.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
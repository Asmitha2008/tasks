print("AIR INDIA TICKET RESERVATION FROM CHENNAI TO BANGALORE")
print("===============================================")
booking_class=input("Enter the booking class (ECONOMY/BUSINESS): ")
if booking_class=="ECONOMY" or booking_class=="BUSINESS":
    print("Your seats are available for this class,enter your seat preference to confirm your reservation")
    seat_preference=input("Enter your seat preference (Window/Aisle/Middle): ")
    if seat_preference=="Window" and booking_class=="ECONOMY":
        print("Your ticket has been booked and the total fare for your reservation is: Rs. 5000")
    elif seat_preference=="Window" and booking_class=="BUSINESS":
        print("Your ticket has been booked and the total fare for your reservation is: Rs. 10000")
    elif seat_preference=="Aisle" and booking_class=="ECONOMY":
        print("Your ticket has been booked and the total fare for your reservation is: Rs. 4500")  
    elif seat_preference=="Aisle" and booking_class=="BUSINESS":
        print("Your ticket has been booked and the total fare for your reservation is: Rs. 9000")
    elif seat_preference=="Middle" and booking_class=="ECONOMY":
        print("Your ticket has been booked and the total fare for your reservation is: Rs. 4000")
    elif seat_preference=="Middle" and booking_class=="BUSINESS":
        print("Your ticket has been booked and the total fare for your reservation is: Rs. 8000")
    else:
        print("Invalid seat preference. Please choose Window, Aisle, or Middle to confirm your reservation.")
    print("Thank you for choosing AIR INDIA")
else:
    print("Sorry, seats are not available for this class. Please choose a different class.")

print("WONDER WOMEN SUPERMARKET")
print("Product: MILK")
#milk brands available in the supermarket
milk_brands=["Amul","Paal pannai","Amma dairies","Mother Dairy","fresh milk","Aavin"]
#product quantity in ml
q_1=250
q_2=500
q_3=1000
#total no of items in the supermarket
no_of_items=150
milk_brands=input("Enter the milk brands you want to buy:")
quantity=int(input("Enter the quantity of milk in ml:"))
no_of_items=int(input("Enter the total number of items you want to buy:"))
if milk_brands=="Amul" or milk_brands=="Paal pannai" or milk_brands=="Amma dairies" or milk_brands=="Mother Dairy" or milk_brands=="fresh milk" or milk_brands=="Aavin":
    print("Milk brand is available in the supermarket.")
    if quantity==250 and no_of_items<=150:
        print("You got 5% discount on this quantity of milk.")
        print("  MRP for 1 unit:RS 30")
        print("  MANUFACTURING DATE:4-5-2026")
        print("  EXPIRY DATE:6-5-2026")
        print("  NET QUANTITY:250ml")
        print("  TOTAL FAT:6%")
        print("  PROTEIN:3.5%")
        print("  CARBOHYDRATES:LACTOSE")
        print("  STORAGE INSTRUCTION:Keep refrigerated at 4°C")
        total_price=30*no_of_items
        print("Total price for your purchase is:",total_price)
        discount=5
        discount_percentage=(total_price*discount)/100
        final_price=total_price-discount_percentage
        print("Final price after discount:",final_price)
        remaining_item=150-no_of_items
        print("Remaining items in the supermarket:",remaining_item)
        print("THANK YOU FOR PURCHASING!!! HAVE A GOOD DAY!!!")
    elif quantity==500 and no_of_items<=150:
        print("You got 10% discount on this quantity of milk.")
        print("  MRP for 1 unit:RS 45")
        print("  MANUFACTURING DATE:4-5-2026")
        print("  EXPIRY DATE:6-5-2026")
        print("  NET QUANTITY:500ml")
        print("  TOTAL FAT:6%")
        print("  PROTEIN:3.5%")
        print("  CARBOHYDRATES:LACTOSE")
        print("  STORAGE INSTRUCTION:Keep refrigerated at 4°C")
        total_price=45*no_of_items
        print("Total price for your purchase is:",total_price)
        discount=10
        discount_percentage=(total_price*discount)/100
        final_price=total_price-discount_percentage
        print("Final price after discount:",final_price)
        remaining_item=150-no_of_items
        print("Remaining items in the supermarket:",remaining_item)
        print("THANK YOU FOR PURCHASING!!! HAVE A NICE DAY!!!")
    elif quantity==1000 and no_of_items<=150:
        print("You got 15% discount on this quantity of milk.")
        print("  MRP for 1 unit:RS 75")
        print("  MANUFACTURING DATE:4-5-2026")
        print("  EXPIRY DATE:6-5-2026")
        print("  NET QUANTITY:1000ml")
        print("  TOTAL FAT:6%")
        print("  PROTEIN:3.5%")
        print("  CARBOHYDRATES:LACTOSE")
        print("  STORAGE INSTRUCTION:Keep refrigerated at 4°C")
        total_price=75*no_of_items
        print("Total price for your purchase is:",total_price)
        discount=15
        discount_percentage=(total_price*discount)/100
        final_price=total_price-discount_percentage
        print("Final price after discount:",final_price)
        remaining_item=150-no_of_items
        print("Remaining items in the supermarket:",remaining_item)
        print("THANK YOU FOR PURCHASING!!! HAVE A GREAT DAY!!!")
    else:
        print("Sorry, we don't have enough stock for the requested quantity.")
else:
    print("Sorry, the requested milk brand is not available in the supermarket.")
        
                   
                     
                
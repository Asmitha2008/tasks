print("ZOMATO")
starter=input("Enter your starter: ")
main_course=input("Enter your main course: ")
dessert=input("Enter your dessert: ")
#starters menu
chicken_soup=150#assignment operator
veg_soup=100
spicycorn_soup=120
#main course menu
chicken_biriyani=250
mutton_biriyani=300
veg_biriyani=200
#dessert menu
mango_icecream=80
falooda=90
brownie=70
if(starter=="chicken soup" and main_course=="chicken biriyani" and dessert=="mango icecream"):#logical operator
    print("you are lucky,you got a BROWNIE FOR FREE")
elif(starter=="veg soup" and main_course=="veg biriyani" and dessert=="falooda"):
    print("you are lucky,you got a MANGO ICECREAM FOR FREE")
else:
    print("TRY A CHICKEN OR VEG COMBO NEXT TIME TO GET A FREE DESSERT")
total_bill=0
if starter=="chicken soup":
    total_bill+=chicken_soup
elif starter=="veg soup":
    total_bill+=veg_soup
elif starter=="spicycorn soup":
    total_bill+=spicycorn_soup
else:
    print("Invalid starter choice")
if main_course=="chicken biriyani":
    total_bill+=chicken_biriyani
elif main_course=="mutton biriyani":
    total_bill+=mutton_biriyani
elif main_course=="veg biriyani":
    total_bill+=veg_biriyani
else:
    print("Invalid main course choice")
if dessert=="mango icecream":
    total_bill+=mango_icecream
elif dessert=="falooda":
    total_bill+=falooda
elif dessert=="brownie":
    total_bill+=brownie
else:
    print("Invalid dessert choice")
print("Your total bill is:",total_bill)
print("WEDNESDAY SPECIAL OFFER: GET 10% OFF ON YOUR TOTAL BILL ")
discount=10
discount_percentage=(total_bill*discount)/100#arithmetic operator
print("Your Total Bill is:",total_bill-discount_percentage)
print("The bitwise operator calculation for chicken_biriyani & mango_icecream is:", chicken_biriyani & mango_icecream)#bitwise operator
print("The bitwise operator calculation for chicken_biriyani | mango_icecream is:", chicken_biriyani | mango_icecream)#bitwise operator
print("THANK YOU FOR PLACING THE ORDER, HAVE A NICE DAY!")


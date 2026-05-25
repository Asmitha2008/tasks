class supermarket:
    def __init__(self, prdt_name="", prdt_id="", prdt_quantity=0, prdt_price=0, prdt_total_price=0):
        self.prdt_name = prdt_name
        self.prdt_id = prdt_id
        self.prdt_quantity = prdt_quantity
        self.prdt_price = prdt_price
        self.prdt_total_price = prdt_quantity*prdt_price
    def show_details(self):
        if self.prdt_total_price > 5000:
            print("YOU ARE ELIGIBLE FOR A DISCOUNT OF 10%")
            discount_amount = self.prdt_total_price * 0.1
            final_price = self.prdt_total_price - discount_amount
            print("FINAL PRICE AFTER DISCOUNT:", final_price)
        else:
            print("YOU ARE NOT ELIGIBLE FOR A DISCOUNT,buy more than 5000 to get a discount")
            final_price = self.prdt_total_price
            print("FINAL PRICE:", final_price)
    def display_product_info(self): 
        print("𝓡𝓔𝓒𝓔𝓘𝓟𝓣 𝓕𝓞𝓡 𝓨𝓞𝓤𝓡 𝓟𝓤𝓡𝓒𝓗𝓐𝓢𝓔:") 
        print(f"     Product Name: {self.prdt_name}")
        print(f"     Product ID: {self.prdt_id}")
        print(f"     Product Quantity: {self.prdt_quantity}")
        print(f"     Product Price: {self.prdt_price}")
        print(f"     Total Price: {self.prdt_total_price}")
        if self.prdt_total_price > 5000:
            print("YOU ARE ELIGIBLE FOR A DISCOUNT OF 10%")
            discount_amount = self.prdt_total_price * 0.1
            final_price = self.prdt_total_price - discount_amount
            print("FINAL PRICE AFTER DISCOUNT:", final_price)
        else:
            print("YOU ARE NOT ELIGIBLE FOR A DISCOUNT,buy more than 5000 to get a discount")
            final_price = self.prdt_total_price
            print("FINAL PRICE:", final_price)
        print("𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐒𝐇𝐎𝐏𝐏𝐈𝐍𝐆 𝐖𝐈𝐓𝐇 𝐔𝐒!") 
print("RETRO ROYALS WELCOMES YOU TO OUR SUPERMARKET!") 
prdt_name = input("ENTER PRODUCT NAME:")
prdt_id = input("ENTER PRODUCT ID:")        
prdt_quantity = int(input("ENTER PRODUCT QUANTITY:"))
prdt_price = int(input("ENTER PRODUCT PRICE:"))
prdt_total_price = prdt_quantity * prdt_price
product = supermarket(prdt_name, prdt_id, prdt_quantity, prdt_price, prdt_total_price)
product.show_details()   
product.display_product_info()

#supermarket
pdt_1="toothpaste"
pdt_2="chocolate"
name_pdts=input("enter the pdt name")
no_of_pdts=int(input("enter the no of pdts need"))
types_of_pdt_1   =["colgate","pepsodent","clove","close up","himalaya hirra"]
types_of_pdt_2   =["fuse", "dairy milk", "choclairs", "oreo dip", "5 star"]
types_of_pdt=input("enter the type_of pdts need")
pdt_2_no_of_pdts=5
pdt_1_no_of_pdts=5
total_no_of_pdts=10
if name_pdts==pdt_1 and no_of_pdts==3:
    print("the product is available")
    print("type of pdt is",types_of_pdt)
    print("no.of pdts need is",no_of_pdts)
    print("the number of products available is",pdt_1_no_of_pdts)
    print("buy three products and get a brush free")
    print("============================================")
    print("pdt description")
    print("manufacturing date=01/06/2026")#manufacturing date
    print("expiring date=01/12/2026")#expiring date
    print("net wt=200g")#quantity
    print("brightens teeth")
    print("calcium boost with argine")
    print("amt per pdt is rs.20")
    print("===========================================")
    print("bill is rs.",no_of_pdts*20)
    print("piece remaining is",pdt_1_no_of_pdts-no_of_pdts)
    print(" total piece remaining is",total_no_of_pdts-no_of_pdts)
elif name_pdts==pdt_1 and no_of_pdts<3:
      print("the product is available")
      print("type of pdt is",types_of_pdt)
      print("no.of pdts need is",no_of_pdts)
      print("the number of products available is",pdt_1_no_of_pdts)
      print("============================================")
      print("pdt description")
      print("manufacturing date=01/06/2026")#manufacturing date
      print("expiring date=01/12/2026")#expiring date
      print("net wt=200g")#quantity
      print("brightens teeth")
      print("calcium boost with argine")
      print("amt per pdt is rs.20")
      print("===========================================")
      print("bill is rs.",no_of_pdts*20)
      print("piece remaining is",pdt_1_no_of_pdts-no_of_pdts)
      print(" total piece remaining is",total_no_of_pdts-no_of_pdts)


if name_pdts==pdt_2 and no_of_pdts==5:
    print("the product is available")
    print("type of pdt is",types_of_pdt)
    print("no.of pdts need is",no_of_pdts)
    print("the number of products available is",pdt_2_no_of_pdts )
    print("buy five products and get a chocolate free")
    print("============================================")
    print("pdt description")
    print("manufacturing date=01/12/2026")#manufacturing date
    print("expiring date=01/12/2027")#expiring date
    print("net wt=200g")#quantity
    print("amt per pdt is rs.10")
    print("===========================================")
    print("bill is rs.",no_of_pdts*10)
    print("piece remaining is",pdt_2_no_of_pdts-no_of_pdts)
    print(" total piece remaining is",total_no_of_pdts-no_of_pdts)


elif name_pdts==pdt_2 and no_of_pdts<3:
         print("the product is available")
         print("type of pdt is",types_of_pdt)
         print("no.of pdts need is",no_of_pdts)
         print("the number of products available is",pdt_2_no_of_pdts )
         print("============================================")
         print("pdt description")
         print("manufacturing date=01/12/2026")#manufacturing date
         print("expiring date=01/1/2027")#expiring date
         print("net wt=200g")#quantity
         print("amt per pdt is rs.10")
         print("===========================================")
         print("bill is rs.",no_of_pdts*10)
         print("piece remaining is",pdt_2_no_of_pdts-no_of_pdts)
         print(" total piece remaining is",total_no_of_pdts-no_of_pdts)
else:
    print("the product is not available")
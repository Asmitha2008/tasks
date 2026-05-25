n=int(input("enter the no of values to be inserted in the list: "))
empty_list=[]
for i in range(n):
    livalue=input("enter the list values")
    empty_list.append(livalue)
print("List values:", empty_list)
index=int(input("enter the index position to insert the value: "))
value=int(input("enter the value to insert: "))
empty_list.insert(index, value)
print("List values after insertion:", empty_list)

#new
list=[1,2,3,4,5]
index=int(input("enter the index position to insert the value: "))
value=int(input("enter the value to insert: "))
list.insert(index, value)
print("List values after insertion:", list)
num=int(input("Enter a number of terms for fibonacci series: "))
a=0
b=1
print("The Fibonacci sequence is:")
for i in range(num):
    print(a, end=" ")
    a,b=b,a+b

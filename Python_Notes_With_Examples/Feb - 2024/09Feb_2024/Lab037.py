# Problem - find the maximun of three numbers
"""a= int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = max(a, b, c)
print(d)
"""
# alternative method
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a > c:
    print("Max number is : ", a)
elif b > a and b > c:
    print("max number is : ", b)
else:
    print("max number is :", c)

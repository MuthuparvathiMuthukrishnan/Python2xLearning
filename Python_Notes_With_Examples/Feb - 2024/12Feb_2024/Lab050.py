#global in python - will be taught later
#Fibonacci series - Fibonaaci meanr sum of the last two digits
#for ex - 0,1,1(0+1),2(1+1)...
"""a = 10
b = 20
#c = a,a+b
#print(type(c))
#print(c)
print(a,a+b)"""

a,b = 0,1
c = int(input("Enter the value: "))
while a < 10:
    a, b = b, a + b
    print(a)



#try, except and finally
#Multiple exception
try:
    num_1 = int(input("Enter num 1 :"))
    num_2 = int(input("Enter num 2 : "))
    num_3 = num_1/num_2
    print(num_3)
except ValueError as v: #instead of any int if we give string we wi get error
    print(v)
except ZeroDivisionError as z: #instead if we divide any value by zero we will get this error
    print(z)
else:
    print(f"Result {num_3}")
finally: #this block will be alwasy executed #not mandatory  but it can be added
    print("i will executed anyhow")



#ValueError : Invalid literal
#Zerodivision

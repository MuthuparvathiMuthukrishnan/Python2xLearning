#Handle Exception
#try and except block
#tru -> try the code
#except - execute except code (it problem try)
a = int(input("Enter num 1 :"))
b = int(input("Enter num 2 : "))
try:
    c = a/b #ZeroDivisionError : division by zero #this error occurs when a value is divided by zero
    print("Div is : ", c)
except Exception as e:
    print(e)
    print("Zero division, please dont use B as Zero")
print("This is important message that we need show to the user")
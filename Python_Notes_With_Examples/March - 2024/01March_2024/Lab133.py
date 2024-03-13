try:
    c = 10/0
except Exception as e:
    print(e)
#zeroDivsionerror
#ValueError
#SyntaxError
#indentationError

#We can use Exception in the except block if we dont
#what error we will be facing in exception
try:
    a = int(input("enter a number only \n"))
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
else:
    print("Else")
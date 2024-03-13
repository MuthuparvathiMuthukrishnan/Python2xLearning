#String
# Bunch of characters
# " " or ' '- can be given as quotes got string
name = 'paru'
name1 = 'Muthu'
print(name,'\n',name1)
print(type(name))
print(type(name1))

dir = r"C:\nbc\nbc.txt" #to print the link as such as it is give 'r' (raw) prior to the link!
print(dir)
#r - this will be useful when we we are giving paths and websites.

#Format String
a = "Muthu"
b = 'parvathi'
age = 28
isMarried = False
print(f"My name is {a}{b}, Your age is {age} , Is she married {isMarried}") #this works with integer as well
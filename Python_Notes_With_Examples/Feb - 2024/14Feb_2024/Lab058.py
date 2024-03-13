#*args and *kwargs
"""def values(a,b=True,c=False):
    d = a + b + c
    print(d)"""
#values(1) #this will give an error asking for the values of other arguments.
# to rectify it we can give the  default values while passing the arguments itself

#give the values in the same order as defined.
#value(c=1,a=2,c=3) #this is not advisable

#*args
"""def sum(a,b,c):
    return a+b+c
r1 = sum(10,11,20)
print(r1)"""

def sum(*args): #*args means any number of arguments
    for i in args:
        print(i)
sum(1,2,3,4,5)

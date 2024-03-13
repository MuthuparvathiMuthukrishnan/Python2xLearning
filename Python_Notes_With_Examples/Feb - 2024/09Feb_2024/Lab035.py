#Condition
#age > 18 - you are allowed to go to the club
#age < 18 - you are not allowed to go the club

age = int(input('You age : '))

if age > 18: #if is a condition based loop
    print("You are allowed to go the club")
else:
    print("You are not allowed to go the club")

a = 8 #this statement can not be given as a condtion in if else
b = 9
if a==b:
    print("Yes they are equal")
else:
    print("No they are not equal")

i = 10
j = 11
if i > j:
    print("i is greater than j")
elif i < j:
    print("i is lesser than j")
else:
    print("i is equal to j")
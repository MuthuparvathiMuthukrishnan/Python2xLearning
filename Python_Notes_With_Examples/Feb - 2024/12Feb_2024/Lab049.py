#Factorial
#n = 5 -> 5*4*3*2*1
#n = 3 -> 3*2*1

number = int(input("Enter the number : "))
fact = 1
if number < 0:
    print("Fact")
elif number == 0:
    print("Fact")
else:
    for i in range(1, number + 1):
        fact = fact * i
print("Factorial: ", fact)
#Create a program that takes two numbers as input and prints whether the
# first number is greater than, less than, or equal to the second number.

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
a = (num_1 > num_2)
b = (num_1 < num_2)
c = (num_1 == num_2)
print("num_1 is greater than num_2",a)
print("num_1 is lesser than num_2",b)
print("num_1 is equal to than num_2",c)
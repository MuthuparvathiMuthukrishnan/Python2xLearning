# Write a Python program to calculate the area of a circle given its
# radius using the formula area=π×r^2 ( Take pie as 3.14)
"""PI = 3.14
r = float(input("Enter the radius : "))
area = PI * r * r
print("Area of the circle is :", area)"""

#Alternative method
import math #importing math  module to caluclate the are of the circle
r = float(input("Enter the radius : "))
print(math.pi)
area = math.pi*pow(r,2) #importing pi from math and then calling the arguments to the power of 2
print(area)


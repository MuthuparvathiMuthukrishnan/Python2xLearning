#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal)
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene
# Eq. = side 1 == side 2 = side 3.

side_1 = float(input('Enter the value of side_1 : '))
side_2 = float(input('Enter the value of side_2 : '))
side_3 = float(input('Enter the value of side_3 : '))
if side_1 == side_2 and side_2 == side_3 and side_1 == side_3:
    print("Equilateral - All sides are equal")
elif side_1 == side_2 and side_2 != side_3 and side_1 != side_3:
    print("Isosceles - Exactly two sides are equal")
elif side_2 == side_3 and side_2 != side_1 and side_3 != side_1:
    print("Isosceles - Exactly two sides are equal")
elif side_3 == side_1 and side_3 != side_2 and side_1 != side_2:
    print("Isosceles - Exactly two sides are equal")
else:
    print("No sides are equal")



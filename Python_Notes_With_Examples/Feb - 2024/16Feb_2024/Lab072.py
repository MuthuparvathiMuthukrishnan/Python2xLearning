#Map()-
# 1. it basically taske seach item form the list and execute the fucntion on it
# 2. Returns the elements as list
#3.

def sq_of_numbers(num):
    return num **2
sq_numbers = sq_of_numbers(4)
print(sq_numbers)

numbers = [1,2,3,4,5,5]
square = list(map(sq_of_numbers,numbers))
print(square)

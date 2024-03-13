#Map is created for lisf of element(list of items ) Map is used when there are multiple items
#map #set #tuples
import math
def sq_root(num):
    return math.sqrt(num)
my_list = [21,34,54]
square = list(map(sq_root,my_list))
print(square)
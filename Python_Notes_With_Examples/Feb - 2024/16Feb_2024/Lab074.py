#filter
#it can filter the itesm from the list based on the logic and returns less of numbers
number = [1,2,3,4,5,6,6,8]
#even_numbers = filter(lambda x:x % 2 ==0, number)
#print(list(even_numbers))
def even_nos(num):
    return num % 2 ==0
    #even_nos = lambda num:num % 2 ==0
even = filter(even_nos,number)
print(list(even))
#print(set(even))

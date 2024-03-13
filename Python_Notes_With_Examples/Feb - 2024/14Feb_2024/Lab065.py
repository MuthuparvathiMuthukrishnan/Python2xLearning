#List
#List - collection of items- duplicates areallowed
#List can have multiple data types
#List index starts fromzero
#List value can be modified

my_list = [1,2,3]
my_list1 = ['a',True,8.90 ]

#indexing
Mmy_list2 = ["Index of list starts from zero "]

#changing an element
my_list3 = [1,2,3,4,5,5,6,]
my_list3[1] = 3 #list value can be changed by mentioning the index of the number and assginig the same
print(my_list3)

#append in list basically adds a new element to the list
my_list3.append(7)#this just adds the value to the  end of the list at the last
print(my_list3)

#extend - adding more than one items to a list
my_list3.extend([68,70,67]) #for extend the values should be given in a square bracket
print(my_list3)

#insert - inserting the element anywhere in the index
my_list3.insert(1,"paru")
print(my_list3)

#remove - removes the value from list
my_list3.remove("paru")
print(my_list3)

#clear -
my_list.clear()
print(my_list)

#copylist
my_list4= my_list3.copy()
print(my_list4)
#reverse of list is also possible
my_list4.reverse()
print(my_list4)

print(my_list4[1])
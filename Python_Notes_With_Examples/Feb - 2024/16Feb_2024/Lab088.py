"""my_dict = {'a' : 1, 'b ': 23, 'c' : 0, 'a': 98, 'd' : 98}
#my_dict1 = dict(a = 1, b = 23,#a = 98#) #this is not allowed it throws syntax error during runtime itself
print(len(my_dict))
print(my_dict)

#other ways to get keys and vales in dict
keys = my_dict.keys()
values = my_dict.values()

keys_list = list(keys)
print(values)"""

my_dict = {'a':1,'b':2}
val = my_dict.pop('a')
print(val)
print(my_dict)

knights = {'gallhand': "the brave", "captain america": "courageous"}
print(knights)

for k,v in knights.items():
    print(k,v)



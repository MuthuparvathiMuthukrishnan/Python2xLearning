set1 = {1,2,3,4,5}
set2 = {5}
set6 = set1.issubset(set2 ) #here set2 is a subset of set1 since all the elements of set2 are present in set1
print(set6)
set7 = set1.issuperset(set2) #here set1 is the superset since all the elements of set2 are in set1
print(set7)

set8 = {'ty0','ly','ty0.'}
print(set8)

for i in set1:
    print(i)
set9 = set([1,2,3,4,5,7,8,9,10,100])
print(set9)
print(type(set9))
set9.remove(1)
set9.remove(100)
print(len(set9))
print(set9)
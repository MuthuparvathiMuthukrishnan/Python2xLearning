name = 'CaptainAmerica'
name1 = 'Spider Man'
print(len(name1)) #len function starts from 1
print(name[-1])
print(name1[7])
print(len(name)-2)
print(name[len(name)-2]) #reading the code from 0 so c is printed
print(len(name))
#strings are stored from 0. that is we ask the index of a string (first letter) it returns zero whereas len starts
# from number 1
#when read from left to right and memory will allocated from 0,1,etc
#if we read right to left memory is allocated from -1

#Strings are immutable
#Strings value can be replce but NOT changed!

a = "Paru"
print(a)
#a[1]='T' #doesnt support
#whereas
a = 'Thangam' #this is possible
print(a)
a = 'Krishnan'
print(a)
name = input("Enter the name : ")
reverse = ""
for i in range(len(name)-1,):
    reverse = name[i] + reverse
    print(reverse)
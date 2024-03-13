str1=input("Enter the main string\n")
str2=input("Enter string which is to be searched\n")

str3=str1.lower()
str4=str2.lower()

# if(str3.find(str4)!=-1):
#     print("Substring present in string")
# else:
#     print("Substring not present in string")

if(str4 in str3):
    print("Substring found")
else:
    print("Substring not found")
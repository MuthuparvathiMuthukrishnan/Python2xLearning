string_1 = input("enter string_1's name :")
string_2 = input("enter string_2's name: ")

if sorted(string_1)== sorted(string_2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")
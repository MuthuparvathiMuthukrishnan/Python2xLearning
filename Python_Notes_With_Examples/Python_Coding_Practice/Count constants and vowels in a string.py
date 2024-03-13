str1=input("Enter a string\n")

vowelCount=0
consonantCount=0

str2=str1.lower()

for i in str2:
    if (i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u'):
        vowelCount = vowelCount + 1
    else:
        consonantCount = consonantCount + 1

print("Count of vowel is", vowelCount)
print("Count of consonant is", consonantCount)
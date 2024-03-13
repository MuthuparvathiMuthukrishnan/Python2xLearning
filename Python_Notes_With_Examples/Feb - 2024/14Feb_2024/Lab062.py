# reverse a string
# palindrome

"""str = "paru"
rev_str = ""
for i in str:
    rev_str = i + rev_str

print(rev_str)"""


# Palindrome using a function
def reverse_str(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("Enter the string value: ")
rev_str = reverse_str("original_str")
if original_str == reverse_str:
    print("Palindrome")
else:
    print("Not a palindrome")

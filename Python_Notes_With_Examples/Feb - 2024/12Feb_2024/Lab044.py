#Break

#for i in range(1,10) - prints the valued form 1 to 9
#BReak is used to break form the loop
# for ex i - 5 > want to break from the loop
"""for i in range(1,10):
    if i == 5: #here the loops prints only until 5 cause i want the loop to break after 5
        break #else is optional in this case
    print(i)
print("Outside the loop")"""

for i in range(1,10):
    print(i) #here the value 5 will be printed because the print is befroe break statement.
    if i == 5: #here the loops prints only until 5 cause i want the loop to break after 5
        break #else is optional in this case

print("Outside the loop")
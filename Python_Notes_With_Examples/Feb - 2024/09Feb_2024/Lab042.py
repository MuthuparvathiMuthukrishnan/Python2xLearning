#write a program that calcualtes and displays the letter grade
# a given numerical score (ed A,B,C,D,E,F)
a = int(input('Enter your score: '))
if a <=100 and a>=90:
    print("Your grade is A")
elif a<=89 and a>=80:
    print('Your grade is B')
elif a <= 79 and a >= 70:
    print('Your grade is C')
elif a <= 69 and a >= 60:
    print('Your grade is D')
elif a<=59 and a>=0:
    print('Your grade is F')
else:
    print("Invalid Input")

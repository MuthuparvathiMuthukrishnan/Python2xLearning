#assignment operator
name ="Krishnan"
#assignment operato stores the vales to its idenfier (variable name = variable value)

#unary operator - single value or single literals
age = +95 #+ is the unary operato
bank_bal = -100 #- is the unary operator
print(age)
print(bank_bal)

#Not operator - Unary - this can be used only with boolean values (True and False)
is_paru_automation_tester_yet = False
print(not is_paru_automation_tester_yet)

# is - operator : identiy operator
a = 1
c = float(2)
print(a is c) #identifies adn returns true/false

#list is stored seprate list. even though the list values are same - it will return false
d = [1,2,3]
d1 = [1,2,3]
print(d is d1)
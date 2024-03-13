#lambda expression
#to help us guys
#Function can written in a single line in python using lambda

"""def greet():
    print("hello")
greet()"""

"""def double_my_salary(salary):
    return salary * 2
result = double_my_salary(10000)
print(result)"""

d_salary = lambda salary: salary*2
print(d_salary(20))

pow = lambda num:num **3
print(pow(16))

sum = lambda a,b : a+b
print(sum(3,5))

name1 = lambda name: print("Your name is : ",name)
name1("Paru")
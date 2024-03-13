#Functions
#Block of code which cna executed
#They can retrun something
#They cant return something - non return type function
#They have parameters
#They dont have parameters/arguments

#defining a function
def say_hello(): #does not return any value without no parameter/argument,
    # here we are simplet defining the function
    print("hello world")  #without calling the funtion - statement will not be printed
say_hello() #calling the function

#same function can be defined by taking arguments/paramters
def say_hello(name):
    # here we are simplet defining the function
    print("hello", name)  #without calling the funtion - statement will not be printed
say_hello("paru") #calling the function
#if arguments is passed while definig functions then while calling the function arguments should be passed

#multiple arguments can be passed while defining functions
def say_hello_args(name, age):
    print(name,age)
say_hello_args("paru",28)

def say_default_name(name="paru"): #here i am definig the argument with values so no need to print the args while calling the functions
    print("My name is : ", name)
say_default_name("Paaru") #even if i call the name - the value which i called while definig gets replaced.

def sum_of_numbers(a,b):
    return a+b
result = sum_of_numbers(10,11)
res_str = sum_of_numbers("Parvathi", "Krishnan")
result3 = sum_of_numbers(a = 10, b = 20)
print(result ,'\n', res_str, '\n', result3)

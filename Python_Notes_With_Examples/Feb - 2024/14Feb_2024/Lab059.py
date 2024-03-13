def make_pizza(*toppings, base): #toppings - that is the word giving , we can give more than one arguments as well
    #for topping in toppings,base: #multiple *args cant be passed as arguments
    print(toppings, base)
    print(type(toppings))
paru = make_pizza("Mushrooms", "Sweet Corn", base = "thick" '\n')
thangam = make_pizza("poori","cauliflower" , base ="thin" '\n')
#give the second argument should be defined while calling the function
print(type(paru))

#def calendar(*months, *number) #this is not possible
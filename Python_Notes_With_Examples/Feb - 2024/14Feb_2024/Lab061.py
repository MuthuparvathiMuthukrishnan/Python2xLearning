def make_pizza(*toppings, base = "Layer crust"):
    print(toppings, base)
    return toppings, base
    #print(type(return))
paru = make_pizza("Mushroom","Sweetcorn")
print(paru)
print(type(paru))
class Person: #the name of the class first letter should be capital
    #class variables or instance variables
    age = None
    name = "muthu"
    #name = None #empty variables cant be empty usually none value is assigned to class variables

    def walk(self):
        a = 10 #local variabe for this method
        print("Hi my name is ", self.name)
        print("Hi my age is ", self.age)
        print(a)

paru = Person()
paru.walk()

parvathi = Person()
parvathi.walk()
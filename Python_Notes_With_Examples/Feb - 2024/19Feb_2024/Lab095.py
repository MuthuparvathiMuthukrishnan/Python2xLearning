#class & objects
#Class - contain attritubes(data members) and behaviours (methods)
#behaviours - methods (not functions) whenever a function is used insisde a class it is called methods.

#person -> object paru, thangam, krishnan
class person:
    #Attributes - Data members
    name = None
    age = None
    height = None
    phone_no = None
    #Behaviours - Methods will called inside a class
    def talk(self):
        print("I can walk")
    def walk(self):
        print("I can talk")
    def sleep(self):
        print("I can sleep")
def another(): #this is a function and it is outside the class #functions are independent
    print("i am a function")

#Object creation #Objects name - ClassName()
a = person()
a.name = "paru"
a.age = 28
print(a.name)

#class is a small space but object takes a block of space for its attritubes and behaviour

#after line 28 the memory gets deleted.
#Hirearchical Inheritance
class Vehicle:
    def information(self):
        return "This is a Vehicle"
class Bicycle(Vehicle):
    def info(self):
        return "This is a Bicycle"
class Car(Vehicle):
    pass
    """def info(self):
        return "This is a Car"""
car = Car()
bicycle = Bicycle()
print(bicycle.info()) #this will return the Car method's value only if this method is not present it will take
#from the parent method.
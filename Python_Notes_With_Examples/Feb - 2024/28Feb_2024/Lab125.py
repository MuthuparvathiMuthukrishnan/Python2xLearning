#Encapsulation
#Inheritance
#Polymorphism - Method overriding and MEthod overloading

#Abstraction
#Abstractio - OOPs
#Hiding the details and showing the what is required
#Do you know how engine is started?
#How gear box was managed
#Hide the implementation adn show only the important details
# 1. Abstract Base Class
# 2. Abstract base Methods

from abc import ABC , abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self): #incomplete method  #whenever we want to enforce something we need to use something
        pass
class Dog(Animal):
    def sound(self):
        return "BOW BOW"

class Cat(Animal):
    def sound(self):
        return "Meow Meow"
dog = Dog('Rancho')
print(dog.sound())
cat = Cat('Cat')
print(cat.sound())
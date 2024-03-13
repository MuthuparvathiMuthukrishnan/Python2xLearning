#Method overriding - same name in the parent and child
#Child always override the parent functions
#Super means call my parent function

class Animal:
    def __init__(self):
        pass
    def sound(self): #both parent and child should haev the same function name
        print("Animal Sound")
class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
        super().sound() #super calls the Animal class
        print("Dog Soung")
animal = Animal()
animal.sound()
dog = Dog()
dog.sound()
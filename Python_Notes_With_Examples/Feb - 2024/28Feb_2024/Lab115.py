#Single Inheritance (Father to Child)
#Multilevel inheritance (Grandparent to Father to Child)
#Multiple Inheritance (two base class  - Father and  Mother and dervied class - Child)
#Hybrid Inheritance
#Hierarchical Inheritance

#API, Web AUtomation - 80% - Single level automation will be used

#Multilevel inheritance

class Grandparent:
    def Grandparent_Method(self):
        return "This is a Grandparent's Method"
class Parent(Grandparent):
    def Parent_Method(self):
        return "This is a Parent Method"
class Child(Parent):
    def Child_Method(self):
        return "This is a Child Method"

child = Child()
print(child.Grandparent_Method())
print(child.Parent_Method())
print(child.Child_Method())


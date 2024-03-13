#Multilevel Inheritance

class GF:
    flat = "FiveBHK"
    def home(self):
        print("I have a home in GOA")
class Father(GF):
    pass
    def home1(self):
        print("I have two homes in Coimbatore")
class Daughter(Father):
    pass
    def home2(self):
        print("I have a new home in Coimbatore")

a = Daughter()
a.home1()
a.home()

b = Father()
b.home2()
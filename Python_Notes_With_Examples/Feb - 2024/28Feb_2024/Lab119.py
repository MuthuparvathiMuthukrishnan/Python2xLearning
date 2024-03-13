#Hybrid Inheritance
# (Single,Multiple, Multilevel inheritance)

class A:
    def MethodA(self):
        return "This is class A"
class B(A):
    def MethodB(self):
        return "This is class B"
class C(A):
    def MethodC(self):
        return "This is Class C"

class D(B,C):
    def MethodD(self):
        return "This is class D (Multiple)"

d = D()
print(d.MethodB())
print(d.MethodA())
print(d.MethodD())
print(d.MethodC())
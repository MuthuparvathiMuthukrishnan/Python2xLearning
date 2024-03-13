class GF:
    def car(self):
        return "Old Car"
class F(GF):
    def car(self):
        return "Honda Civic"
class S(F):

    def car(self):
        return "Audi"
son = S() #read the preceeding method if the current method is not present
print(son.car())
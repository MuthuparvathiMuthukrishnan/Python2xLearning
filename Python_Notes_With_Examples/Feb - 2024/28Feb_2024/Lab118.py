#Multiple Inheritance

#F,M -> S

class Father:
    def father_money(self):
        return "5"
    def home(self):
        return "This is from Father"
class Mother:
    def mother_money(self):
        return "2"
    def home(self):
        return "This is from Mother"
class Son(Mother): #whatever name we pass as arguments here will be called for the Son functions
#if this method doess  not have any methods then the arguments will be called upon
    def home(self):
        return "This is son's amount"

son = Son()
print(son.home())
print(Son.mro()) #MEthod Resoultion Order #this lets us know what method will be rea first
#print(son.father_money())


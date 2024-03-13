#car -
#objects - Tesla, lambo

class Car():
    name = None
    speed = None
    color = None
#self is a special variable that is used within the context of OOPs - Object oriented programming language
#It is a reference to the instance of a class
#access and manipulates the attritubes of that instance/ object


    def start_engine(self):
        print("Starting engine")
    def drive(self):
        print("drive")
    def car_break(self):
        print("car break", self.name)
    def who_is_driving(self):
        print("I am driving the car", self.name) #self is the instance of the to access the class attritubes.
tesla_obj = Car()
lambo_obj = Car()

#tesla_obj.name = "Tesla"
#lambo_obj.name = "lambo"

tesla_obj.car_break()
lambo_obj.car_break()

print()
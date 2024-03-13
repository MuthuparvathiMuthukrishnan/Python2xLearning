#to solve this hard code problom in class variable we got CONSTRUTOR

class Car:
    name = None
    model = None
    make = None

    #when parametrised constructor is present a non parametrised constructor is not allowed.
    """def __int__(self):
        print("HI")"""
    def __init__(self, c_name,c_model,c_make): #parametrised construtor
        #Special function. it will be automatically called whenever a f(n) is created.
        self.name = c_name
        self.model = c_model
        self.make = c_make
    def start_engine(self):
        print("Car name", self.name)
        print("Car model", self.model)
        print("Car make", self.make)

lambo = Car("Lambo", "v2", 2024)
lambo.start_engine()

alto = Car('SWIFT', 'NEW', 2021)
alto.start_engine()

"""ferrari = Car()
Car.start_engine()"""
class Myclass:
    def __init__(self):
        print("Public function")
        self.name = 'Paru'

    def public_fun(self):
        print("This is a public function")

    def __private_fun(self): #privaet function which is part of the class Re allowed in that class only
        print("This is a private function")

    def public_n_private(self): #this can call privaet function cause this is within class
        print("This is a public private function")
        self.__private_fun()
        #encapsulation - if you are encapsulated in the class you can call the privaet class.
        #security
a= Myclass
a.public_fun("fdfd")
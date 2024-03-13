class Home:
    def info(self):
        return "This is my father's home"
class Paru(Home): #if value is present in the calling method then that value will be printed as output
                    #else the parent method's value will be called.
    """def info(self):
        return "This is my Home"""
    pass
class Thangam(Home):
    def info(self):
        return "This is my home too"

paru = Paru()
print(paru.info())

#Single inheritance

class Father:
    gold = 5
    __private_villa = "GOA" #wont be able to access by the son class
    def car(self):
        print("Lambo")
    def ThreeBHKFlast(self):
        print("yes three bhk flat is available")
    def pub_private(self,is_auth):
        if is_auth:
            print("allowed", self.__private_villa)
        else:
            print("NO")

class Son(Father): #inheritance from the Father class
    pass

Paru = Son()
Paru.car()
Paru.pub_private(False)
print(Paru.gold)

mm = Father()
mm.car()

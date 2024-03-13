from abc import ABC , abstractmethod

class ATB(ABC):

    @abstractmethod
    def perform_task1(self): #incomplete method  #whenever we want to enforce something we need to use something
        pass

    @abstractmethod
    def perform_task2(self):  # incomplete method  #whenever we want to enforce something we need to use something
        pass
class Paru(ATB):
    def perform_task1(self):
       return "Bow Bow"

    def perform_task2(self):
        return "Meow Meow"
paru = Paru()
print(paru.perform_task1())
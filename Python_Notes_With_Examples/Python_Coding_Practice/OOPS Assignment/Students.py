class Student:
    name=None
    phoneNumber=None
    address=None
    idCardNumber=None

    def attendSchool(self):
        print("Attending school")

    def enterPersonalDetailsInRegister(self):
        print("Entering phone number")

    def enterNameInAttendance(self):
        print("Name in attendance sheet")

    def getIDCard(self):
        print("Get ID card")

ram=Student()
ram.getIDCard()
ram.attendSchool()
ram.enterNameInAttendance()
ram.enterPersonalDetailsInRegister()

shyam=Student()
shyam.enterNameInAttendance
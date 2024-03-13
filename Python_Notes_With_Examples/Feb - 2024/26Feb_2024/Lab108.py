class Secureclass:
    def submit(self):
        self.__username = "paru"
        self.__password = "123"
        self.heading = "VWOheading"
        print(1, self.heading)

    def public_private(self):
        print("i am a private method", self.__username)
a = Secureclass()
a.submit()
a.public_private()
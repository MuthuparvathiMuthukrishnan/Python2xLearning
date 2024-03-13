class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var = 20

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid password")
    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Not allowed, weak password")
pwd = Password("poiuy@134")
pwd.get_password(True)
pwd.set_password("paru#1234")

#private and protectec variables can be only called by functions. 
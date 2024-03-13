class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message) #exception constructor

balance = 100
withdraw_amount = int(input("Enter the amount you can withdraw"))
if withdraw_amount > balance:
    raise MyCustomException("Bal is low!")
else:
    print("Remaining amount is : ", balance - withdraw_amount)

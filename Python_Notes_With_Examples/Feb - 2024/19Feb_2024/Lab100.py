class Car:
    name = None
    color = None
    def car_details(self):
        print("Your car details are : ", self.name, self.color)
car_name = input("Enter the name of the car : ")
car_color = input("Enter the colour of the car : ")

car_obj_ref = Car()
car_obj_ref.name = car_name
car_obj_ref.color = car_color
car_obj_ref.car_details()

from faker import Faker

#create a Faker instance
fake = Faker()

#generate a fake name
print(fake.name())
#output  might be something like John Doe

#Generate a fake address
print(fake.address())
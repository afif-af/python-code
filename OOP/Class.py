class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled Over!")
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

#Working with Classes and Instances

class Car:

    def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
    def get_descriptive_name(self):

            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

print("\n")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print("\n")

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("\n")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self,mileage):
        self.odometer_reading=mileage
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)

my_new_car.update_odometer(10)
my_new_car.read_odometer()


print("\n")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self,mileage):
       if mileage>=self.odometer_reading:
           self.odometer_reading=mileage
       else:
           print("you canit roll back an odomete! ")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_used_car= Car('subaiu','outback',2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


#inheritance

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self,mileage):
       if mileage>=self.odometer_reading:
           self.odometer_reading=mileage
       else:
           print("you canit roll back an odomete! ")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class ElectricCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())






from car import ElectricCar
my_leaf=ElectricCar('nissan','leaf',2022)
print(my_leaf.get_descriptive_name())
my_leaf.battery.get_range()
my_leaf.battery.describe_battery()
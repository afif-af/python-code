amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount * 0.15
    print(" Discount", discount)
print(" Net payable:", amount - discount)

var = list[0, 1, 2, 3, 4, 5]
for var in list(range(5)):
    print(var)

for let in 'Bangladesh':
    print('current letter', let)

for i in range(1, 11):
    for j in range(1, 11):
        k = i * j
        print(k, end=' ')

    print()

no = int(input('any number: '))
numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]
for num in numbers:
    if num == no:
        print('number found in list')
        break
else:
        print('number not found in list')

for letter in 'Python':  # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
     print(car.upper())
  else:
    print(car.title())
car = 'Audi'
x=car.lower() == 'audi'
print(x)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
   print(f"{user.title()}, you can post a response if you wish.")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
     print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
     if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
     else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
     for requested_topping in requested_toppings:
         print(f"Adding {requested_topping}.")
     print("\nFinished making your pizza!")
else:
     print("\nAre you sure you want a plain pizza?")


# Using multiple List
available_toppings =['mushrooms','olives','green peppers',
                     'pepperoni','pineappe','extra cheese']
requested_toppings =['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we donot have {requested_topping}.")
print("\n Finished making your pizza!")
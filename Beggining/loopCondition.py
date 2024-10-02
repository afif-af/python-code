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

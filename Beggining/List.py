list = ['asf', 798, 6.4, 'fjlk']
addlist = [687, 'afif']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(addlist * 2)
print(list + addlist)
# adding element to the end a list

motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
print(motorcycle)

motorcycle.insert(0, 'bmw')
print(motorcycle)

# remove an item
del motorcycle[0]
print(motorcycle)
# last element delete
popped_motorcyle = motorcycle.pop(0)
print(motorcycle)
print(popped_motorcyle)
motorcycle.remove('suzuki')
print(motorcycle)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

len(cars)

# Looping Through an Entire List

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
     print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

message="hello python world"
print(message)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")

for i in range(1,5):
    print(i)

squares=[]
for value in range(1,11):
    square = value ** 2
    squares.append(squares)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares=[value ** 2 for value in range(1,11)]
print(squares)

# Looping Through a Slice

players=['charles','martina','michael','florence','eli']
print("here are the first theww players on my team")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

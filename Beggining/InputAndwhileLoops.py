message=input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# while loop
current_number = 1
while current_number <= 5:
      print(current_number)
      current_number += 1

#prompt="\n Tell me something, and i wiil repeat it back to you :"
#prompt+="\n enter quite to end the program "
#message =""
#while message !='quit':
  #  message=input(prompt)
  #  print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
 # message = ""
# while message != 'quit':
   # message = input(prompt)
   # if message != 'quit':
    #    print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active=True
while active:
    message=input(prompt)
    if message == 'quit':
        active= False
    else:
        print(message)


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
     city = input(prompt)

     if city == 'quit':
        break
     else:
      print(f"I'd love to go to {city.title()}!")

current_number = 0
while current_number < 10:
      current_number += 1
      if current_number % 2 == 0:
          continue
      print(current_number)


# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
      current_user = unconfirmed_users.pop()
      print(f"Verifying user: {current_user.title()}")
      confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
      pets.remove('cat')
print(pets)


responses={}
#Set a flag to indicate that polling is active
polling_active=True
while polling_active:
    name=input("\n what is your name ?")
    response=input("which mountain would you like to climb someaday?")

    responses[name]=response
    repeat= input("Would you like to let another person respond? (yes/ no) ")
    if repeat== 'no':
        polling_active=False
print("Polling result : ---")
for name ,response in responses.items():
    print(f"{name} would like to climb {response}")








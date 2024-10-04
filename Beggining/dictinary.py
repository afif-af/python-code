dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = { 'name': 'afif', 'code': 86, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

alien_0={'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

my_points=alien_0['points']
print(f"You just earned {my_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0={}
alien_0['color']='blue'
alien_0['points']=20
print(alien_0)

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"original positionL:{alien_0['x_position']}")
if alien_0['speed']== 'slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print(f"new position :{ alien_0['x_position']}")


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
language=favorite_languages['sarah'].title()
print(f"sarah favorite language is {language}")

alien_0={'color': 'green','points': 5}
del alien_0['points']
print(alien_0)

# alien_0={'color': 'green'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# loop

user_0 ={
    'username':'efemi',
    'first':'enrico',
    'last' : 'fermi',
 }
for key,value in user_0.items():
    print(f"\n key : {key}")
    print(f"value : { value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name,language in favorite_languages.items():
    print(f"{name.title()} falvorite language is{ language.title()}")

for name in favorite_languages.keys():
    print(name.title())
friends =['phil','sarah']
for name in favorite_languages.keys():
    print(f"\n Hi {name.title()}")

    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t {name.title()}, i see you love {language}")



if 'erin' not in favorite_languages.keys():
    print("Erin ,please take our poll ")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool")


languages = {'python', 'rust', 'python', 'c'}
print(languages)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
     print(alien)

aliens=[]
for alien_number in range(30):
    new_alien ={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:6]:
    print(alien)
print("....")
print(f"total numbers of aliens: {len(aliens)}")



# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (30):
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
     aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

pizza={
    'crust':'think',
     'toppings':['mushrooms','extra cheese'],
}

print(f"you orderesd a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
     print(f"\n{name.title()}'s favorite languages are:")
     for language in languages:
          print(f"\t{language.title()}")

users={
    'aeinstein':
        {
            'first':'albert',
            'last':'einstein',
            'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}


for username,user_info in users.items():
    print(f"Username:{username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    print(f"\t Full name : {full_name.title()}")
    print(f"\t Location:{location.title()}")















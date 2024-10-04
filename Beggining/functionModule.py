def greet_user(username):
    print(f"Hello, {username.title()}")

greet_user('afif')


def describe_pet(animal_type, pet_name):
    print(f"\ni Have a {animal_type}")
    print(f"My {animal_type} is name is {pet_name}")

describe_pet('Hamster', 'harry')
describe_pet(animal_type='dog', pet_name='willie')

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('williew')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('john','hooker','lee')
print(musician)

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name,age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']=age
    return person
musician = build_person('jimi', 'hendrix',age=22)
print(musician)



def get_formatted_name(first_name, last_name):
    full_name = f"{first_name}  {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name=input("first name: ")
    if f_name=='q':
        break
    l_name=input("last name: " )
    if l_name=='q':
        break

    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\n Hello, {formatted_name}")

def greet_users(names):
    for name in names:
        msg=f"hello, {name.title()}"
        print(msg)

usernames=['Afif','Afroz','Fahim']
greet_users(usernames)

unprinted_designs=['phone case','robot pendant','dofecahedron']
completed_models=[]

while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"printing model : {current_design}")
    completed_models.append(current_design)

print("\nthe following models have been printed")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model : {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print(F"\nthe following models have been printed :")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)


def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first,last,**user_info):
    user_info['fist_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='physics')
print(user_profile)

























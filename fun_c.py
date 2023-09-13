def greet_user():
    print("Hello User!")

greet_user()


def greeting(user_name) :
    print(f'Hello ,{user_name.title()}!')


greeting("bruno")


def describe_pet(animal_type,pet_name) :
    print(f'I have a {animal_type} .')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

print(describe_pet('hamster','harry'))




####### new code #########

def get_formatted_name(first_name, second_name, middle_name=''):

    if middle_name:

        full_name = f"{first_name} {middle_name} {second_name}" 
    else:

        full_name = f"{first_name} {second_name}" 
    return full_name.upper()

musician= get_formatted_name('\n \n Beijuka', 'Bruno') 

print(musician)


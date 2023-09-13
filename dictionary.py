# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Accessing values using keys
print(my_dict['key1'])  # Output: value1

# Modifying values
my_dict['key2'] = 'new value'
print(my_dict['key2'])  # Output: new value

# Adding a new key-value pair
my_dict['key4'] = 'value4'

# Removing a key-value pair
del my_dict['key3']

# Checking if a key exists
if 'key3' in my_dict:
    print('Key exists')
else:
    print('Key does not exist')  # Output: Key does not exist

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)




#   EXERCISE


person = {
    'first_name': 'Beijuka',
    'last_name': 'Bruno',
    'age': 21,
    'city': 'Netlabs UG Cedat'
}

print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])




favorite_numbers = {
    'Bruno': 7,
    'Nickson': 22,
    'Charles': 23,
    'Diana': 2,
    'Sam': 0
}

for name, number in favorite_numbers.items():
    print(name + "'s favorite number is:", number)


# favorite_numbers = {}
#
# for _ in range(5):
#     name = input("Enter a friend's name: ")
#     number = int(input("Enter their favorite number: "))
#     favorite_numbers[name] = number
#
#
#
# for name, number in favorite_numbers.items():
#     print(name + "'s favorite number is:", number)
#
#


    # Exercise 6-4


capitals = {
    'Kampala': 'Uganda',
    'Nairobi': 'Kenya',
    'Dodoma': 'Tanzania',
}


for capital, country in capitals.items():
    print("The", capital, "of the country is ", country + ".")

# Printing the name of each river
print("\nNames of the capitals:")
for capital in capitals.keys():
    print(capital)

# Printing the name of each country
print("\nNames of the countries:")
for country in capitals.values():
    print(country)





#  user imput () function

message = input("Tell me something , and I will repeat it back to you: ")
print(message)


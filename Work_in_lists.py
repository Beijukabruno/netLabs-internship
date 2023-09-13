
# using range() function

for value in range(1,10):
    print(value)
numbers=list(range(1,10))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


# Square numbers
squares = []

# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)

for value in range(1,11):
    squares.append(value**2)
print(squares)





# LIST COMPREHENSION

sq_numbers = [value**2 for value in range(1,11)]
print(sq_numbers)



even=[value**2 for value in range(2,11,2)]
print(even)

print(even_numbers[::-1])
print(sq_numbers[::-1])



# TUPLES



dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])



favorite_pizzas = ['Pepperoni', 'Margherita', 'Supreme']

# Printing the name of each pizza
print("Printing the names of my favorite pizzas:")
for pizza in favorite_pizzas:
    print(pizza)

# Printing a sentence using the name of each pizza
print("\nPrinting a sentence about each pizza:")
for pizza in favorite_pizzas:
    print("I like", pizza, "pizza.")

# Printing additional lines about how much I like pizza
print("\nI really love pizza!")

# animals = ["dog", "cat", "rabbit"]
#
# for animal in animals:
#   print(f"A {animal} would make a great pet!")
#
# print("\nAny of these animals would make a great pet!")

animals = ['Dog', 'Cat', 'Rabbit']

# Printing the name of each animal
print("Names of the animals:")
for animal in animals:
    print(animal)

# Printing a statement about each animal
print("\nStatements about each animal:")
for animal in animals:
    print("A", animal.lower(), "would make a great pet.")

# Printing a statement about what these animals have in common
print("\nAny of these animals would make a great pet!")


# Printing numbers from 1 to 20
for number in range(1, 21):
    print(number)

numbers = list(range(1, 1000001))

for number in numbers:
  print(number)


# Creating a list of odd numbers from 1 to 20
odd_numbers = list(range(1, 21, 2))

# Printing each number using a for loop
for number in odd_numbers:
    print(number)


# Creating a list of multiples of 3 from 3 to 30
multiples_of_3 = [num for num in range(3, 31) if num % 3 == 0]

# Printing each number using a for loop
for number in multiples_of_3:
    print(number)

# Creating a list of the first 10 cubes
cubes = [num**3 for num in range(1, 11)]

# Printing each cube using a for loop
for cube in cubes:
    print(cube)
    
# Generating a list of the first 10 cubes using a list comprehension
cubes = [num**3 for num in range(1, 11)]

# Printing the list of cubes
print(cubes)

# Generating a list of even numbers from 2 to 20
even_numbers = [num for num in range(2, 21, 2)]

# Printing the list of even numbers
print("The list of even numbers:", even_numbers)

# Printing the first three items in the list
print("The first three items in the list are:", even_numbers[:3])

# Printing three items from the middle of the list
middle_start = len(even_numbers) // 2 - 1
middle_end = middle_start + 3
print("Three items from the middle of the list are:", even_numbers[middle_start:middle_end])

# Printing the last three items in the list
print("The last three items in the list are:", even_numbers[-3:])







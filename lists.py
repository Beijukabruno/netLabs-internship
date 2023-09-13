bicycles=['trek','cannodle','redline','specialiszed']
print(bicycles)

# sets can not have duplicates
#
motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

del bicycles[0]
print(bicycles)

# del, sort, pop, reverse ,len

cars =['BMW', 'audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True) # this is doing the reverse.... desending order
print(cars)

print(len(bicycles)  ,len(cars))


# print(cars[4])

names = ["John", "Jane", "Mary","Bruno","Nickson","Vinald"]
for name in names:
#   print(name)

  # special message
   message = f"Hello, {name}! you are most welcome to Netlabs UG!."
# for name in names:
   print(message)

# alaways ident after a for loop


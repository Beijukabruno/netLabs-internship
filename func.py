import coffee
# from coffee import coffee_additives


# import coffee
# def coffee_additives(additives):
#     for additive in additives:
#         print(additive, 'has been added')
#     print('Thank you')


additive_list =[]

add = input('Enter additive to be added to your coffee (or type q to quit): ')

while add != 'q':

    additive_list.append(add.title())
    add = input('Enter another additive to be added to your coffee (or type q to quit): ')

coffee.coffee_additives(additive_list)

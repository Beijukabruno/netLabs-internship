# Create an empty dictionary
# my_dict = {}
glossary = {
    'variable': 'A named storage location in memory that holds a value.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control flow statement that iterates a set of instructions until a certain condition is met.',
    'list': 'An ordered collection of items that can be of different types.',
    'conditional statement': 'A statement that performs different actions based on whether a certain condition is true or false.',
    'name': 'My name is Beijuka Bruno. '
}
# Prompt the user for input
user_input = input("Enter a key for the item (or 'q' to quit): ")

# Continue prompting the user until they enter 'q'
while user_input != 'q':
    # Prompt the user for the corresponding value
    value_input = input("Enter the definition for the item: ")

    # Add the key-value pair to the dictionary
    glossary[user_input] = value_input

    # Prompt the user for the next key, or 'q' to quit
    user_input = input("Enter a key for the item (or 'q' to quit): ")

# Print the resulting dictionary
print("\nFinal Dictionary:\n", glossary)
print("\n \n")

for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")











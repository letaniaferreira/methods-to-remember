# Pet Names

# Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.
# For example, 'ziggy': 'canary'
# Put at least 3 key-value pairs in your dictionary.
# Use a for loop to print out a series of statements such as "Willie is a dog."

def animals(animals_name, animals_type):
    """takes in tow list and creates a dictionary using zip"""

    animals_dict = {}

    for name, kind in zip(animals_name, animals_type):
        animals_dict[name] = kind

    for kv in animals_dict.items():
        print(kv[0] + ' is a ' + kv[1])
   


animals(['ziggy', 'melo', 'dandi'], ['canary', 'dog', 'bear'])

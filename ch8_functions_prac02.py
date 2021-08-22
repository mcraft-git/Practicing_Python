
# Function parameters can be defined with default values.
def describe_pet(animal_name,animal_type='cat'):
    """Prints pet's name and species."""

    print(f"My pet is a {animal_type} named {animal_name.title()}.")

# If no argument is passed for the parameter, the default value is used.
describe_pet('ichi')

# Keyword arguments can be used in any order.
describe_pet(animal_type = 'dog', animal_name = 'annie')
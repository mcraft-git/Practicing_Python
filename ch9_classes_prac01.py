
# Let's practice classes!

# A class name should be capitalized in Python. 
class Cat:
    """Builds simulated cat models."""

    # A function that is part of a class is called a Method.
    # To create an Instance of a class, '__init__' is required.
    # The '__init__' method is already baked into Python...
    # ...it runs automatically whenever we create a class (once we define it).
    def __init__(self, name, age):
        """Initializes name and age attributes."""

        # The prefix 'self' makes a variable available to every method in a class.
        # These accessible variables are called Attributes.
        self.name = name
        self.age = age
    
    # The 'self' parameter is required in each method definition, which
    # allows instances to refer to themselves automatically in method calls.
    def nap(self):
        """Simulate a cat napping."""

        print(f"{self.name} is having a nap.")
    
    def meow(self):
        """Simulate a cat's meow."""

        print(f"{self.name} meows at you. (Did human forget dinner?)")
    
    # Other parameters besides 'self' can be defined.
    def swipe(self, target):
        """Launch a simulated cat attack."""

        # Just remember to make them available if necessary.
        self.target = target
        print(f"{self.name} swipes at {self.target}! It's a critical hit!")

# Creating an instance of the 'Cat' class,
# and passing arguments for the attributes.
my_cat = Cat('Ichi',10)

print(f"My cat's name is {my_cat.name}. He is {my_cat.age} years old.")

# Calling class methods.
# Notice that 'self' is not passed as an argument.
my_cat.nap()
my_cat.meow()
my_cat.swipe("foot")
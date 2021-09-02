
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
cat1 = Cat('Ichi',10)

print(f"My cat's name is {cat1.name}. He is {cat1.age} years old (middle-aged in cat years).")

# We can create as many instances of a class as we need.
cat2 = Cat('Ryuko',1)

print(f"Sabrina's cat's name is {cat2.name}. At just {cat2.age} year old, she is still a kitten!")

# Calling class methods.
# Notice that 'self' is not passed as an argument.
cat1.nap()
cat1.meow()
cat2.swipe("foot")
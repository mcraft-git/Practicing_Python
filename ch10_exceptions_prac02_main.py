
# Let's practice with files and exceptions.
# We've saved our functions in the next module,
# so let's import them alogn with the 'random' library.
import random
from ch10_exceptions_prac02_module import BookParser as BP

# Now we will create string variables to
# store the paths of saved texts in this directory. 
# Sadly, I don't actually have 'Pippi.txt'...
book1 = 'Crash_Course_2\\Alice1.txt'
book2 = 'Crash_Course_2\\Alice2.txt'
book3 = 'Crash_Course_2\\Anne1.txt'
book4 = 'Crash_Course_2\\Anne2.txt'
book5 = 'Pippi.txt'

my_books = [book1,book2,book3,book4,book5]

# Here we'll use the 'random.choice()' function
# to pick a random book and copy it to a variable.
selection = random.choice(my_books)

# Finally, the string containing the stored path is passed
# to the imported class and an instance of 'BookParser' is created.
# (see prac02_module)
BP(selection)
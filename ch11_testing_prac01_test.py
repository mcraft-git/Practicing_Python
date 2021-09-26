
# It's important to test functions so that we know they are
# working as intended. Python's 'unittest' module does just that.
# First let's import the module into our test file. 
import unittest

# Next, we'll import the function we want to test.
from ch11_testing_prac01_module import get_formatted_name

# Now we create a class called 'NamesTestCase' that we will use to
# contain a series of defined unit tests with which to test our function.
# This will be a child class that must inherit from the class 'unittest.TestCase'.
# (So Python will know how to run the tests we write)
class NamesTestCase(unittest.TestCase):
    """Tests for 'ch11_testing_prac01_module.py'."""

    # Here's the first test function.
    def test_first_last_name(self):
        """Do names like Georges St-Pierre work?"""

        formatted_name = get_formatted_name("Georges","St-Pierre")

        # The 'assertEqual' method of this class verifies that a result
        # received matches the result that was expected.
        self.assertEqual(formatted_name, "Georges St-Pierre")

# This if block is included to run the test file
# if it is the main program.
if __name__ == '__main__':
    unittest.main()

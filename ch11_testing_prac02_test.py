
# We just tested functions, so now let's test a class!
import unittest
from ch11_testing_prac02_module import AnonymousSurvey as AS

# We create a new TestCase class that inherits 'unittest.TestCase'
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    # Using the unittest 'setUp()' method lets us create an instance of
    # the class we are testing. Python runs the setUp() method
    # before each method starting with "test_" in the TestCase class.
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""

        question = "What's your favorite gaming device?"
        self.my_survey = AS(question)
        self.responses = ['PC','Playstation','Xbox']


    def test_store_single_response(self):
        """Test that a single response is stored properly."""

        # This method will use an instance created by 'setUp()'
        # to copy the first item in the "self.responses" list,
        # and append it to the newly created list in the "self.my_survey" instance
        # by using our "AS" class method "store_response()".
        self.my_survey.store_response(self.responses[0])

        # It will then run the unittest method 'assertIn()'
        # to verify that the item was stored.
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_responses(self):
        """Test that three responses are store properly."""

        # This method uses a FOR loop to iterate over all the "self.responses" list items,
        # and copy each one to the newly created list in the "self.my_survey" instance.
        # (Remember, each method gets its own fresh instance)
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


# (Remember to include the code below if this test file isn't the main program)
if __name__ == '__main__':
    unittest.main()

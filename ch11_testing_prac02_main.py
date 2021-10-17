
from ch11_testing_prac02_module import AnonymousSurvey as AS

question = "What's your favorite gaming device?"
my_survey = AS(question)

my_survey.show_question()
print("Enter 'q' at any time to quit. \n")

while True:

    response = input("Device: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
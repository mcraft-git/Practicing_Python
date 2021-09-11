
# More fun with files!

participants = []
all_accounted = False

while all_accounted == False:

    participant = input("Time for another mandatory poll! Please enter your name: ")
    participants.append(participant.title())

    new_user_chk = input("Next in line?(y/n): ")
    if new_user_chk.lower() == "n":
            all_accounted == True
            break

print(participants)

# When we pass 'w' to open() as the 2nd argument
# the file passed as the 1st argument is overwritten (so BE CAREFULL).
# If there is no file with the given name, Python creates one (include extension).
with open('pet_poll_answers.txt','w') as file_object:
    file_object.write("TOTALLY LEGIT POLL RESULTS\n")

for participant in participants:
    animal_type = input(f"{participant}, which would you prefer to have as a pet - dog or cat?\n")
    animal_type = animal_type.lower()

    # The 'replace()' method replaces its 1st argument with the 2nd.
    # Remember: strings in Python are immutable,
    # so make sure to copy the result to a variable as below.
    animal_type = animal_type.replace('dog','cat')

    # When we pass 'a' as the 2nd argument to open(),
    # Python appends the string to the file.
    with open('pet_poll_answers.txt', 'a') as file_object:
        file_object.write(f"{participant}: {animal_type.title()}\n")

print("\nThank you for involuntarily participating. Now, lets have those results!\n")

with open("pet_poll_answers.txt") as file_object:
    contents = file_object.read()
    # We can use the 'count()' method to add up the total
    # number of occurences of the argument passed.
    # Below, the total number of lines is saved to "lines".
    lines = contents.count('\n') - 1

print(contents.rstrip())

print(f"\nWould you look at that?? This impartial poll has provided an un-biased,"
f"completely coincidental consensus! All {lines} of you prefer cats!")


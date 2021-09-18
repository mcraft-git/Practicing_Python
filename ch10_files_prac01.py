
# Let's work with some files!
# The keyword 'with' closes the file when the program is finished,
# which we always want to do (otherwise corruption or loss may occur).
# Another way would be with 'close()'.
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
# Including the 'rstrip()' method removes the blank line left by 'read()'.    
print(contents.rstrip())

print("")
# This version looks for the file "hello binary.txt"
# in a subfolder of the current directory.
with open('Crash_Course_2/hello_binary.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# We can also use the full file path, however backslashes
# used in Windows directories must be doubled (see example below).
# This is because a single backslash is used to escape characters.

# Saving a path as a variable is common practice.
# full_file_path = 'C:\\This\\is\\where\\the\\path\\goes\\buncha_lines.txt'
file_path = 'Crash_Course_2\\buncha_lines.txt'

with open(file_path) as file_object:

    # To work a file's contents outside of the 'with' block,
    # we can use the 'readlines()' method
    # and assign the created list to a variable ("lines").
    lines = file_object.readlines()

    # We can use a loop to parse each line,
    # which is great for searching a file.
for line in lines:

    # Don't forget to rstrip!
    print(line.rstrip())

# Let's print() an edited version of the contents of pi_digits.txt.
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # We've overwritten the previous example here. 
    lines = file_object.readlines()

# Create an empty string to store the lines...
pi_string = ''

# ...then append each line after using 'strip()' to remove whitespace.
for line in lines:
    pi_string += line.strip()

print(pi_string)

# If we wanted to print less numbers we could throw in a slice.
print(f"{pi_string[:4]}...")

# Find out how long a string is by wrapping
# the 'len()' method around a string object.
print(len(pi_string))

# We can search a string's contents easily with an IF statement.
bday_chk = input("Enter your birthday (ddmm): ")
if bday_chk in pi_string:
    print(f"Jeepers! Your birthday ({bday_chk}) is in the first 31 digits of Pi!")
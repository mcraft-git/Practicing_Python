
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
file_path = 'C:\\Users\\craft\\00_codez\\Python\\Crash_Course\\Crash_Course_2\\buncha_lines.txt'

with open(file_path) as file_object:

    # To work a file's contents outside of the 'with' block,
    # we can use the 'readlines()' method
    # and assign the created list to a variable ("lines").
    lines = file_object.readlines()

    # We can use a loop to parse each line,
    # which is great for searching a file.
for line in lines:
    # Don't forget to strip!
    print(line.rstrip())
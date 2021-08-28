
# Functions can return any kind of value, including lists and dictionaries.
# Optional parameters are given the default value of "None".
def build_person(first_name, last_name, middle_name=None,age=None):
    """Returns a dictionary of attributes."""

    # Create an empty dictionary.
    person = {'first': first_name, 'last': last_name}

    # Add keys and values IF conditions are met.
    if middle_name and age:
        person['middle_name'] = middle_name
        person['age'] = age
    elif middle_name:
        person['middle_name'] = middle_name
    elif age:
        person['age'] = age
    
    return person

print("Welcome to the personal profile builder!\n")

fname = input("Please enter your first name: ")
fname = fname.lower()
lname = input("\nPlease enter your last name: ")
lname = lname.lower()
mname = input("\nPlease enter your middle name (or leave blank): ")
if mname:
    mname = mname.lower()
age = input("\nPlease enter your age (or leave blank): ")

# Send optional arguments IF inputs are received.
if mname and age:
    profile = build_person(fname,lname,mname,age)

elif mname:
    profile = build_person(fname,lname,mname)

# Due to the order of positional arguments,
# we must pass a "None" value for 'mname' under this condition...
# (even though the function parameter has a default value of "None").
elif age:
    profile = build_person(fname,lname,None,age)

else:
    profile = build_person(fname,lname)

# Prints the profile as an unformatted dictionary.
print(f"Thanks! Here's your profile:\n{profile}")
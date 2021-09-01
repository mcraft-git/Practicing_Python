
# Let's use functions to make a program that builds toys!

# When importing, shorten the module name
# with 'as' to make calls easier.
import ch8_functions_toybuilder_module as tm

print("A toy is waiting to be born and become your new friend!\n"
    "But it needs your help figuring out what sort of toy it will be...\n")

toy_type = input("What type of toy is it (enter a number)?"
"\n\t1. Teddy Bear\n\t2. Dress-up Dolly\n\t3. Rowdy Robot\n>")
toy_type = int(toy_type)
if toy_type == 1:
    toy_type = "Teddy Bear"
elif toy_type == 2:
    toy_type = "Dress-up Dolly"
else:
    toy_type = "Rowdy Robot"

print(f"A {toy_type}? Great choice!\n"
    f"Now just answer the following questions to build your {toy_type}."
    "\nPlease type the exact spelling of each part as displayed to ensure we can create the toy you want.\n")

# This line calls the function 'toy_parts' from a module...
# ...while using the module's shortened import name: 'tm'
# It passes the 'toy_type' argument to the function
toy_parts_fin = tm.toy_parts(toy_type)

# Before this next line is run, the 'toy_parts' function
# will have returned the 'parts' dictionary
# and copied it to memory allocated for the 'toy_parts_fin' variable
# (see definition in the module file)

toy_name = input("\nWhat is its name?\n>")

# The final line passes the Positional Arguments 'toy_type' and 'toy_name'
# to the 'toy_specifications' function defined in the module file

# The Arbitrary Keyword Argument 'toy_parts_fin' is passed last...
# ...Arbitrary arguments have asterisks and must always be passed
# AFTER "non-arbitrary" Positional and Keyword Arguments
# (1 asterisk = tuple | 2 asterisks = dictionary)
tm.toy_specifications(toy_type,toy_name,**toy_parts_fin)

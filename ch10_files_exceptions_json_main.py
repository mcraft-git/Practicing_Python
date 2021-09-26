
# Let's practice writing to files using JSON.
# (See module file for comments on function definitions)
import ch10_files_exceptions_json_module as m

prompt01 = input("New user? (y/n): ")

if prompt01 == 'y':
    m.create_new_username()

else:
    old_username = m.find_old_username()

# If there was file and a match (a string value was returned), the old user is greeted.
if old_username:
    print(f"Welcome back, {old_username}! I shall weep not, for the memory lives on...\n"
    "...\nAttempting to load 'mclachlan.midi'...\n...\nLoad failed. ;_;")
    quit()

# If there was no file ('None' was returned), the user is prompted to create one.
# (See module definition for handling if a file exists, but there's no username)
else:
    prompt02 = input("Record not found. Would you like to be the *first* to create a username?! (y/n): ")

if prompt02 == 'y':
    m.create_new_username()
else:
    quit()
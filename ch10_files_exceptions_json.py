
# Let's practice writing to files using JSON.
# (See module file for comments on function definitions)
import ch10_files_exceptions_json_module as m

prompt01 = input("New user? (y/n): ")

if prompt01 == 'y':
    m.create_new_username()

else:
    old_username = m.find_old_username()

# If there was file and a match, the old user is greeted.
if old_username:
    print(f"Welcome back, {old_username}! I shall weep not, for the memory lives on...\n"
    "...\nAttempting to load 'mclachlan.midi'...\n...\nLoad failed. ;_;")
    quit()

# If there was no file, the user is prompted to create one.
else:
    prompt02 = input("Record not found. Would you like to be the *first* to create a username?! (y/n): ")

if prompt02 == 'y':
    m.create_new_username()
else:
    quit()

# The JSON format is commonly used to store and share data.
# To use it in a Python program, we must first import the 'json' module.
import json

username_file = "usernames.json"

def create_new_username():
    """Creates new username file, or adds new username to existing file."""

    new_username = input("\nWhat will your username be?\n> ")
    new_username = new_username.lower()
    
    # Since we want to store usernames in a JSON file, we can save user inputs
    # as dictionaries to make them easier to manage ("usr_dict").
    # And since we want this program to store multiple individual usernames (as JSON),
    # we can create a list variable ("usr_dict_list") to store the dictionaries.
    usr_dict_list = []
    usr_dict = {
        'name':new_username,
        }
    
    # The 'json.dumps()' method converts a Python object into a JSON string.
    # (The 's' stands for 'string')
    # We can specify the indent, and print it for viewing if we like.
    json_obj = json.dumps(usr_dict, indent = 4)
    print(json_obj)

    json_ok = input("Is this okay? (y/n): ")
    if json_ok == 'y':

        # We'll set a try block to catch the 'FileNotFound' exception,
        # so that we can create a new json file if there isn't one already.
        try:

            # If a json file exists, we'll load it with 'json.load()'
            # We can't use 'json.loads()' because we are saving these usernames
            # as json (list) objects, not just as a string.
            # (Again, the 's' in 'json.loads' stands for 'string')
            with open(username_file,'r') as f:
                usr_dict_list = json.load(f)
            
            # Next, we append the new username dictionary to our list.
            usr_dict_list.append(usr_dict)

            # Then we will write the list back to the file,
            # overwriting the old data with 'w' so that only the newly
            # appended list is saved.
            with open(username_file, 'w') as f:
                json.dump(usr_dict_list,f)

            print(f"I will remember you, {new_username}. Will you remember me?")
            quit()

        except FileNotFoundError:

            # If no file is found, we will append our list with the new username,
            usr_dict_list.append(usr_dict)

            # then use the 'a' argument to create a new file
            # and copy the data over into a json format by using 'json.dump()'.
            with open(username_file, 'a') as f:
                json.dump(usr_dict_list,f)
            
            print(f"I will remember you, {new_username}. Will you remember me?")
            quit()

    else:

        # Otherwise, if the user doesn't like the username displayed in json format
        # they can go back to try another one out.
        # (It was just an excuse to use 'json.dumps()' anyway...)
        create_new_username()


def find_old_username():
    """Checks file for username."""

    old_user_check = input("Please enter your username: ")
    old_user_check = old_user_check.lower()

    # We set 'try' in case there's no file...
    try:

            # ...then we will load the current list of users with 'json.load()'...
            with open(username_file, 'r') as f:
                old_user_list = (json.load(f))

            # ...and iterate over it to check against the input for a match.
            for name in old_user_list:
                if name['name'] == old_user_check:
                    return name['name']

            # If a file is found, but no match is found, then the "create_new_username" function is called. 
            print("\nWe could not find your username.\n")
            create_new_username()

    # If no file is found, then this function returns 'None'
    # (see main file for next step)
    except FileNotFoundError:
        return None



def get_fn_input():
    """Obtains user input for the first name."""

    in_fn = input("Please enter a first name: ")
    return in_fn



def get_ln_input():
    """Obtains user input for the last name."""

    in_ln = input("Please enter a last name: ")
    return in_ln



 

def get_formatted_name(first_name,last_name):
    """Returns a formatted name."""

    if first_name and last_name:
        formatted_name = (f"{first_name} {last_name}")
        formatted_name = formatted_name.title()
        return formatted_name
    else:
        print("You must enter a first and last name.")
        return None

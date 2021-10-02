
def get_fn_input():
    """Obtains user input for the first name."""

    in_fn = input("Please enter a first name: ")
    return in_fn


def get_mn_input():
    """Obtains user input for the middle name (optional)."""

    in_mn = input("Please enter a middle name, or just press enter if you don't have one: ")
    if in_mn:
        return in_mn
    else:
        return None


def get_ln_input():
    """Obtains user input for the last name."""

    in_ln = input("Please enter a last name: ")
    return in_ln


 

def get_formatted_name(first_name,last_name,middle_name =""):
    """Returns a formatted name."""

    if middle_name:

        if first_name and last_name:
            formatted_name = (f"{first_name} {middle_name} {last_name}")
            formatted_name = formatted_name.title()
            return formatted_name
        else:
            print("You must enter a first and last name.")
            return None
    else:

        if first_name and last_name:
            formatted_name = (f"{first_name} {last_name}")
            formatted_name = formatted_name.title()
            return formatted_name
        else:
            print("You must enter a first and last name.")
            return None


# This is a module file. Function definitions are saved in modules.
# The main file of a program will import functions from modules.


# Notice the double asterisk before the "parts" parameter,
# which indicates an arbitrary number of Keyword Arguments
# may be passed to the function as 'key=value' pairs.
def toy_specifications(toytype,toyname,**toyparts):
    """Builds profile of desired toy. Prints build status."""



def toy_parts(**toytype):
    """Prints questionaire to obtain inputs.
        Compiles list of desired parts."""

    parts = {}

    if toytype == 1:
       parts['fur'] = input("What kind of fur does the Teddy Bear have?"
        "\nOptions:\n\tsoft black\n\tshaggy brown\t\npolar\n>")
       parts['style'] = input("What's the Teddy Bear holding?"
        "\nOptions:\n\ta bee hive\n\ta fish\t\na honey jar\n>")
       parts['style'] = input("What does the Teddy Bear wear?"
       "(leave blank for a plain 'ol bear)"
        "\nOptions:\n\ta raincoat\n\ta bumblebee costume\n>")



def toy_complete(spec):
    """Prints completed toy profile."""
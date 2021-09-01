
# This is a module file. Function definitions are saved in modules.
# The main file of a program will import functions from modules.

def toy_parts(toytype):
    """Prints questionaire to obtain inputs.
        Compiles list of desired parts."""

    parts = {}

    if toytype == "Teddy Bear":
       parts['fur'] = input("\nWhat kind of fur does your Teddy Bear have?"
        "\nOptions:\n\tsoft black\n\tshaggy brown\n\tpolar\n>")
       parts['held'] = input("\nWhat's your Teddy Bear holding?"
        "\nOptions:\n\tbee hive\n\tfish\n\thoney jar\n>")
       parts['outfit'] = input("\nWhat does your Teddy Bear wear?"
       " (leave blank for a plain 'ol bear)"
        "\nOptions:\n\traincoat\n\tbumblebee costume\n>")
       # This statement deletes the 'outfit' key if input is blank
       if parts ['outfit'] == "":
           del parts['outfit']
    
    if toytype == "Dress-up Dolly":
       parts['skin'] = input("\nWhat skin tone does your Dress-up Dolly have?"
        "\nOptions:\n\tdark\n\tmedium\n\tlight\n>")
       parts['hair'] = input("\nWhat kind of hair does your Dress-up Dolly have?"
        "\nOptions:\n\tpoofy black\n\tcurly brunette\n\tstraight blonde\n>")
       parts['outfit'] = input("\nWhat is your Dress-up Dolly wearing?"
       "(leave blank for a simple white dress)"
        "\nOptions:\n\tyellow springwear\n\tblue swimsuit\n\tred ballgown\n>")
       if parts['outfit'] == "":
            del parts['outfit']


    if toytype == "Rowdy Robot":
       parts['base'] = input("\nHow does your Rowdy Robot move around?"
        "\nOptions:\n\ttank treads\n\tbionic legs\n\thovercraft\n>")
       parts['arms'] = input("\nWhat does your Rowdy Robot have for arms?"
        "\nOptions:\n\tspring-loaded fists\n\tmagnetic drills\n\tdouble lasers\n>")
       parts['head'] = input("\nWhat sits on top of your Rowdy Robot's frame?"
        "\nOptions:\n\ttalking head\n\tsuper-brain tank\n\tsonic siren\n>")

    return parts 


# Notice the double asterisk before the "parts" parameter,
# which indicates an arbitrary number of Keyword Arguments
# may be passed to the function as 'key=value' pairs.
def toy_specifications(toytype,toyname,**toyparts):
    """Builds profile of desired toy. Prints build status."""

    print(f"\nORDER PLACED! We are building your toy! (see details below)\nToy type: {toytype}\nToy name: {toyname}\nSelected features:\n"
    f"\t{toyparts}")

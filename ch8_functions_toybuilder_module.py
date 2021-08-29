
# This is a module file. Function definitions are saved in modules.
# The main file of a program will import functions from modules.

# 
# Notice the double asterisk before the "parts" parameter,
# which indicates an arbitrary number of Keyword Arguments
# may be passed to the function as 'key=value' pairs.
def toy_specifications(type,name,**parts):
    """Builds profile of desired toy. Prints profile."""
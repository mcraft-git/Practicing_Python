
# Functions start with the keyword 'def'
# This function is defined with the parameter 'username'
def greet_user(username):
    """This is a docstring.
        Docstrings should explain what a function does."""

    print(f"Hello, {username.title()}!\n")

# Input is passed to the function call as an argument
username = input("\nWhat's your name?\n")
greet_user(username)

# Docstrings will display if a function is passed to the 'help' method
help(greet_user)
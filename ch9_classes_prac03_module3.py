
import ch9_classes_prac03_module1 as mod1
import ch9_classes_prac03_module2 as mod2

# This is the first function called by the program.
# It requires classes from module1 and module2 (thus the imports).
def create_account():
    """Determines which account type to create."""

    print("\nSo... you think you're pretty funny?\n"
    "Then why not join our super exclusive, super hilarious community of comedic narcissists?\n")

    username = input("Enter a username: ")
    joined = input("Enter today's date (mm/dd/yyyy): ")
    password = input("Enter a password: ")
    admin_pass = input("If you're an admin, do the thing: ")

    # Input is checked as a conditional to determine what the class should be.
    if admin_pass == "hysterical admin":

        # "Admin" class is called (see module2) and passed input args,
        # then the instance is copied to variable 'admin'.
        # Method 'show_privileges' is called from class instance,
        # (displays privileges to user).
        # Login class (see module1) is called and passed 'admin' instance.
        admin = mod2.Admin(username, joined, password)
        admin.show_privileges()
        mod1.Login.login_prompt(admin)

    else:

        # "User" class is called (see module1).
        pleb = mod1.User(username,joined,password)
        pleb.show_privileges()
        mod1.Login.login_prompt(pleb)

# This function allows additional new users to be created.
def user_type_prompt():
    """Checks whether user is new."""

    user_type = input("\nNew user? (y/n)")
    if user_type == "y":
        create_account()
    elif user_type == "n":
        print("Okay, we're done here.")
        quit()
    else:
        print("Sorry, we don't serve liminals.")
        quit()

import ch9_classes_prac03_module1 as mod1
import ch9_classes_prac03_module2 as mod2

def create_account():
    """Determines which account type to create."""

    print("\nSo... you think you're pretty funny?\n"
    "Then why not join our super exclusive, super hilarious community of comedic narcissists?\n")

    username = input("Enter a username: ")
    joined = input("Enter today's date (mm/dd/yyyy): ")
    password = input("Enter a password: ")
    admin_pass = input("If you're an admin, do the thing: ")

    if admin_pass == "hysterical admin":

        admin = mod2.Admin(username, joined, password)
        admin.show_privileges()

    else:

        pleb = mod1.User(username,joined,password)
        pleb.show_privileges()

def user_type_prompt():
    """Checks whether user is new."""

    user_type = input("\nNew user? (y/n)")
    if user_type == "y":
        create_account()
    elif user_type == "n":
        mod1.Login.login_prompt()
    else:
        print("Sorry, we don't serve liminals here.")

from ch9_classes_prac03_module2 import Admin
import ch9_classes_prac03_module3 as mod3

class User:
    """Builds profile instances."""

    def __init__(self, username, joined, password):
        """Instantiates individual profiles."""

        self.username = username
        self.joined = joined
        self.password = password
        self.login_attempts_counter = 0
        self.account_lock = False
        self.privileges = ["can add post"]
        self.admin_user = False
        self.store_profile(self.username,self.joined,self.password)

    
    def show_privileges(self):
        """Displays list of privileges."""

        print(f"\nHere's what you can do on the Funny Forum...\n{self.privileges}")

    
    def display_user(self):
        """Displays user details during account creation."""

        print(f"Here are your details:\n"
        f"\tusername: {self.username}\n"
        f"\tjoined: {self.joined}\n"
        f"\tpassword: {self.password}")


    def store_profile(self,username,joined,password):
        """Stores user profiles."""

        user_list = []
        new_user = {'user':username,'join':joined,'pw':password}
        user_list.append(new_user)


class Login:
    """
    Verifies user login credentials.
    Locks user account if attempt threshold reached.
    """

    def __init__(self):
        """Instantiates login attempt."""


    def login_prompt(self):
        """Prompts for user password."""

        print("\nYou will now need to login to access the boards."
        " This may seem silly, but humor us.")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        self.login(username,password)


    def login(self, username,password):
        """Checks input user password."""

        for user in User.user_list:

            if username == user('user') and password == user('pw'):
                print(f"\nWelcome, {username}!"
                " You have access to the Funny Forum. Don't be a Karen.\n")
                mod3.user_type_prompt()
            else:
                self.login_attempts()


    def login_attempts(self):
        """
        Increments login attempts.
        Locks account after three failed attempts.
        """

        while self.account_lock == False:
            
            if self.login_attempts_counter < 3:
                self.login_attempts_counter += 1
                print("Try again bruh...\n")
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
    
            for user in User.user_list:

                if username == user('user') and password == user('pw'):
                    print(f"\nWelcome, {username}!"
                    " You have access to the Funny Forum. Don't be a Karen.\n")
                    mod3.user_type_prompt()

                else:
                    self.account_lock = True
                    print(f"This account has been locked due to failed logins."
                    " You probably weren't that funny anyway.")
                    
                    if self.admin_user == True:
                        self.login_reset_prompt()
                        break
                    else:
                        break


    def login_reset_prompt(self):
        """Prompt for admin reset password."""

        admin_pw = input(f"Admin:\nTo unlock, you know what to do: ")
        self.login_reset(admin_pw)


    def login_reset(self,password):
        """Resets user account login."""

        if password == "hysterical admin":
            self.account_lock = False
            print(f"{self.username}'s account has been unlocked. Sweet redemption is yours!"
            " (Don't screw this up.)")
            self.login_prompt()
        else:
            print("zhjsbcfjkfdc\n"
            "Okay, you got us. Failing the reset is pretty funny.")
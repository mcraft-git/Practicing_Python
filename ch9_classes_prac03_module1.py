
import ch9_classes_prac03_module3 as mod3

class User:
    """Builds profile instances."""

    # An __init__ instantiates a class instance with its attributes.
    def __init__(self, username, joined, password):
        """Instantiates individual profiles."""

        # These are the attributes of the class "User".
        self.username = username
        self.joined = joined
        self.password = password
        self.login_attempts_counter = 0
        self.account_lock = False
        self.admin_user = False
        self.privileges = ["can add post"]
        # An attribute can call a method.
        # (this dictionary is for demonstrative purposes, but is otherwise unnecessary)
        self.user_list = self.store_profile(self.username,self.joined,self.password)

    
    def show_privileges(self):
        """Displays list of privileges."""

        print(f"\nUsers, here's what you can do on the Funny Forum...\n{self.privileges}")

    
    def store_profile(self,username,joined,password):
        """Stores user profiles."""

        user_list = {}
        user_list['user'] = username
        user_list['join'] = joined
        user_list['pw'] = password
        return user_list


class Login:
    """
    Verifies user login credentials.
    Locks user account if attempt threshold reached.
    """

    def login_prompt(self):
        """Prompts for user password."""

        print("\nYou will now need to login to access the boards."
        " This may seem silly, but humor us.")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        Login.login(self,username,password)


    def login(self,username,password):
        """Checks input user password."""

        # Here's why the dictionary isn't necessary:
        # We can always check the attributes of a class...
        # ...as long as 'self' is passed.
        if self.username == username and self.password == password:
            print(f"\nWelcome, {username}!"
            " You have access to the Funny Forum. Don't be a Karen.\n")
            mod3.user_type_prompt()
        else:
            Login.login_attempts(self)


    def login_attempts(self):
        """
        Increments login attempts.
        Locks account after three failed attempts.
        """

        # In order to '.get' from our dictionary attribute,
        # we must first copy it to a variable in the method definition.
        # (I'm not sure why this is required... but I'm a n00b!)
        userlist = self.user_list
        while self.account_lock == False:
            
            if self.login_attempts_counter < 3:
                self.login_attempts_counter += 1
                print("Try again bruh...\n")
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
                # Now we can '.get' those key values...
                u = userlist.get('user')
                p = userlist.get('pw')
                # ...and check them against inputs.
                if username == u and password == p:
                    self.login_attempts_counter = 0
                    print(f"\nWelcome, {username}!"
                    " You have access to the Funny Forum. Don't be a Karen.\n")
                    # Calls function that allows additional users to be created.
                    # Notice that 'self' is not sent.
                    mod3.user_type_prompt()

            else:
                self.account_lock = True
                print(f"This account has been locked due to failed logins."
                " You probably weren't that funny anyway.")

                # Checks attribute flag to determine if user is admin,
                # because admins can unlock accounts!    
                if self.admin_user == True:
                    Login.login_reset_prompt(self)
                else:
                    quit()


    def login_reset_prompt(self):
        """Prompt for admin reset password."""

        admin_pw = input(f"Admin:\nTo unlock, you know what to do: ")
        Login.login_reset(self,admin_pw)


    def login_reset(self,password):
        """Resets user account login."""

        if password == "hysterical admin":
            self.account_lock = False
            print(f"{self.username}'s account has been unlocked. Sweet redemption is yours!"
            " (Don't screw this up.)")
            Login.login_prompt(self)
        else:
            print("zhjsbcfjkfdc\n"
            "Okay, you got us. Failing the reset is pretty funny.")

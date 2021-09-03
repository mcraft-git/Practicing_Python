
"""
Module file for the 'User' class.
This class builds user profiles for a web forum.
"""

# Now let's practice modifying a class's attributes.
class User:
    """Builds profile instances."""

    # The attributes that may be modified are:
    # 'login_attempts_counter' (counter) and 'account_lock' (boolean flag).
    # The methods modifying these attributes simulate a user login policy.
    def __init__(self, username, joined, password):
        """Instantiates individual profiles."""

        self.username = username
        self.joined = joined
        self.password = password
        self.login_attempts_counter = 0
        self.account_lock = False
    

    def display_user(self):
        """Displays user details during account creation."""

        print(f"Here are your details:\n"
        f"\tusername: {self.username}\n"
        f"\tjoined: {self.joined}\n"
        f"\tpassword: {self.password}")


    # This method takes an input from the user,
    # then passes it as an argument to another method.
    def login_prompt(self):
        """Prompts for user password."""

        print("\nYou will now need to login to access the boards."
        " This may seem silly, but humor us.")
        password = input("Please re-enter your password: ")
        self.login(password)


    # This method calls another method if a condition is not met.
    def login(self, password):
        """Checks input user password."""

        if self.password == password:
            print(f"Welcome, {self.username}!"
            " You have access to the Funny Forum. Don't be a Karen.")
        else:
            self.login_attempts()


    # This method modifies both the counter and the flag
    # if the user continues to enter incorrect passwords.
    # The counter is modified to 0 if password is correct.
    def login_attempts(self):
        """
        Increments login attempts.
        Locks account after three failed attempts.
        """

        while self.account_lock == False:
            
            if self.login_attempts_counter < 3:
                self.login_attempts_counter += 1
                password = input("Try again bruh: ")
    
                if password == self.password:
                    self.login_attempts_counter = 0
                    self.login(password)
                    break

            else:
                self.account_lock = True
                print(f"This account has been locked due to failed logins."
                " You probably weren't that funny anyway.")
                self.login_reset_prompt()
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
    
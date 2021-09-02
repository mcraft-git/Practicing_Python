
# Now let's practice modifying a class's attributes.
class User:
    """Builds user profiles for a web forum."""

    def __init__(self, username, joined, password):
        """Instantiates user profiles."""

        self.username = username
        self.joined = joined
        self.password = password
        self.login_attempts_counter = 0
        self.account_lock = False
    

    def login(self, password):
        """Checks input user password."""

        if self.password == password:
            print(f"Welcome, {self.username}! You have access to the Funny Forum. Don't be a Karen.")
        else:
            self.login_attempts()


    def login_attempts(self):
        """
        Increments login attempts.
        Locks account after three failed attempts.
        """
        while self.account_lock == False:
            
            if self.login_attempts_counter < 3:
                self.login_attempts_counter =+ 1
                password = input("Try again bruh: ")
                if password == self.password:
                    self.login(password)
                    break
                else:
                    continue
            else:
                self.account_lock == True
                print(f"This account has been locked due to failed logins."
                "You probably weren't that funny anyway.")
    

    def login_reset(self,password):
        """Resets user account login."""

        if password == "hysterical admin":
            self.account_lock == False
            print(f"{self.username}'s account has been unlocked. Sweet redemption is yours!"
            "(Don't screw this up.)")
        else:
            print("zhjsbcfjkfdc\n"
            "Hah!\nOkay, you got us. Failing the reset is pretty funny.")


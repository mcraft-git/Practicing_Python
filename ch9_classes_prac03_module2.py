
# Let's import a class from another module into this one.
# We will use it to create a child class.
from ch9_classes_prac03_module1 import User

# Now lets create a child class named 'Admin',
# from the parent class 'User'. (Congratulations, User!)
class Admin(User):
    """Builds Admin profile instances."""
    
    def __init__(self,username,joined,password):
        """Instantiates individual admin profiles."""
        
        # The 'super()' function can call a method from the parent class.
        # By calling '__init__' we give the Admin instance all the parent attributes.
        super().__init__(username,joined,password)

        # This attribute name matches an attribute name from the parent,
        # hence the child attribute overrides the parent's.
        self.privileges = ["can ban user","can un-ban user","can unlock account",
        "can add posts","can delete posts"]
        
        self.admin_user = True

    # Defining a method that matches the name of a parent method overrides the parent.
    def show_privileges(self):
        """Displays list of privileges."""

        print(f"\nAdmins, here's what you can do on the Funny Forum...\n{self.privileges}")
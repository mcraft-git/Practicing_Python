
# Main program for ch9_prac02

# We can import a whole module, or just its classes.
# Let's do an explicit import of a class from this module.
# (...even through there's just one class in there)
from ch9_classes_prac02_module import User

print("\nSo... you think you're pretty funny?\n"
"Then why not join our super exclusive, super hilarious community of comedic narcissists?\n")

username = input("Enter a username: ")
joined = input("Enter today's date (mm/dd/yyyy): ")
password = input ("Enter a password: ")

# Since we explicity imported the class,
# we can call it without a prefix.
user1 = User(username,joined,password)

user1.display_user()

user1.login_prompt()

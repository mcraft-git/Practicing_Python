
# Main program for ch9_prac02

import ch9_classes_prac02_module as m

print("So... you think you're pretty funny?\n"
"Then why not join our super exclusive, super hilarious community of comedic narcissists?\n")

username = input("Enter a username: ")
joined = input("Enter today's date (mm/dd/yyyy: ")
password = input ("Enter a password: ")

user1 = m.User(username,joined,password)

print(f"Here are your details:\n"
"\tusername: {user1.username}\n"
"\tjoined: {user1.joined}\n"
"\tpassword: {user1.password}")

print("You will now need to login to access the boards."
"This may seem silly, but humor us.")
password = input("Please re-enter your password: ")

user1.m.login(password)
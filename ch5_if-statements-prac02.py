
# the keywords 'in' and 'not' can be used to check for items in a list
banned_users = ['derpster','toxicguy','datkaren']
user = "noob"
if user not in banned_users:
    print(f'{user} may join the forum.')

# methods such as 'lower()' are often used with statements
print('\n')
user = 'ToxicGuy'
if user.lower() in banned_users:
    print(f'NOPE. Nice try, {user} (AKA {user.lower()}).')

# keywords 'if', 'else', and 'elif' can be used to test multiple conditions
ages = [12,26,3,74,42,8]
print('\n')
for age in ages:
    if age < 4:
        price = 0

    elif age < 18:
        price = 10

    elif age < 64:
        price = 25

    else:
        price = 10
    # but perhaps 'elif >=65' would be easier to read
    print(f'You are {age} years old. Your cost of admission is: ${price}.')
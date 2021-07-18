
# there are several ways to loop through a dictionary, such as a FOR loop
user_1 = {
    'username': 'BdB',
    'first': 'Brittany',
    'last': 'Del Bryant'
}

# using two variables to store the key and value pairs; and also the keyword '.items()'
for key, value in user_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# using the dictionary from before
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'darlene': 'c#'
}
for n, l in favorite_languages.items():
    print(f"\n{n.title()}'s favorite language is {l.title()}.")

# if we just wanted the names (keys) for the people in our dictionary, we would use the method '.keys()'
for k in favorite_languages.keys():
    print(f"{k.title()}")
print("\n")

# looping through a dictionary with an IF chain condition
friends = ['darlene', 'sarah']
for n in favorite_languages.keys():
    print(f"Hi, {n.title()}.")
    # below, the value of the key 'n' is returned from the dictionary and copied to variable 'l'
    if n in friends:
        l = favorite_languages[n].title()
        print(f"\t{n.title()}, I see you like {l}!")

# We can use the .keys() method to check if a key is in a list
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

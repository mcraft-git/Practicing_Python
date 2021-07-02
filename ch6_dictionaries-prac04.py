
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
}
for n, l in favorite_languages.items():
    print(f"\n{n.title()}'s favorite language is {l.title()}.")

# if we just wanted the names (keys) for the people in our dictionary, we would use the keyword '.keys()'
for k in favorite_languages.keys():
    print(f"{k.title()}")
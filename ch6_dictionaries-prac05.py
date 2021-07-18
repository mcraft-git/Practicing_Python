favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'darlene': 'c#'
}
# We can return a sorted list of keys by wrapping '.keys()' with 'sorted()'
for n in sorted(favorite_languages.keys()):
    print(f"{n.title()}, thank you for taking our poll!")

# We can use the '.values()' method to return a values from a list
# This will include duplicate values
print("\nThe following languages have been mentioned in our poll:")
for l in sorted(favorite_languages.values()):
    print(f"\nThe {l.title()} programming language.")

# To return only unique values, we use the '.set()' method
# Sets will not sort items in any specific order, so wrap with .sorted()
print("\nThe following unique languages have been mentioned in our poll:")
for l in sorted(set((favorite_languages.values()))):
    print(f"\nThe {l.title()} programming language.")

# We can build a set directly using braces and separating elements with commas
# Unlike dictionaries, sets are not composed of key:value pairs
language_set = {'Python','C','C#','Ruby','Python'}

print(f"\nLook Ma, no dupes: {language_set}")
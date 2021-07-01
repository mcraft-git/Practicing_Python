
# Dictionaries can be used to store information about many objects (like people).
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Using variables to store information pulled from a dictionary is good practice.
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# We can delete keys from dictionaries.
del favorite_languages['phil']
print(favorite_languages)

# The preferred way to pull values from a dictionary is the GET method, which will return a default value if the key is not found.
# The automatic default is 'none', but a different value can be set manually.
# Using the GET method can avoid errors.
alien_03 = {'speed': 'slow', 'x_pos': 0}
point_value = alien_03.get('points', 'No point value assigned.')
print(point_value)
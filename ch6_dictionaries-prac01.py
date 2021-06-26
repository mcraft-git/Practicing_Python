
# a dictionary in Python is a collection of key-value pairs
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# new key-value pairs can be added to an existing dictionary
print('\n')
print(alien_0)

# we might add x-coordinate (left to right) and y-coordinate (upper to lower) positions
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

print(alien_0)

# we can create an empty dictionary to fill later (possibly with user inputs)
print('\n')
alien_1 = {}

alien_1['color'] = 'blue'
alien_1['points'] = 10
alien_1['x_pos'] = 0
alien_1['y_pos'] = 25

print(alien_1)

# we can change the value of a key stored in a dictionary (use double quotes for the string!)
print(f"The alien is currently {alien_1['color']}.")
alien_1['color'] = 'red'
print(f"The alien is now {alien_1['color']}.")
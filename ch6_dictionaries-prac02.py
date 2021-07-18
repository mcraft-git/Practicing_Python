
# let's track the movements of these aliens
alien_0 = {'name': 'alien_0', 'speed': 'slow', 'x_pos': 0}
alien_1 = {'name': 'alien_1', 'speed': 'medium', 'x_pos': 0}

# dictionaries can be elements in a list, which is called 'Nesting'
alien_squad = [alien_0, alien_1]

for alien in alien_squad:

    print(f"{alien['name']} has an x-coordinate of {alien['x_pos']} on the grid.\n")

# we can use IF statements to assign values to variables based on key values in dictionaries
for alien in alien_squad:
    if alien['speed'] == 'slow':
        x_increment = 1
    elif alien['speed'] == 'medium':
        x_increment = 2
    elif alien['speed'] == 'fast':
        x_increment = 3
    alien['x_pos'] = alien['x_pos'] + x_increment
    print(f"{alien['name']} now has an x-coordinate of {alien['x_pos']} on the grid!")

# let's give our second alien a speed boost and run our IF chain again
alien_1['speed'] = 'fast'
print('\n')

for alien in alien_squad:
    if alien['speed'] == 'slow':
        x_increment = 1
    elif alien['speed'] == 'medium':
        x_increment = 2
    elif alien['speed'] == 'fast':
        x_increment = 3
    alien['x_pos'] = alien['x_pos'] + x_increment
    print(f"{alien['name']} now has an x-coordinate of {alien['x_pos']} on the grid!")
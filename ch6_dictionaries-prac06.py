# Now let's use Nesting again to make a whole fleet of aliens!
aliens = []

# Use a loop with the range() method to spawn 30 green aliens (the grunts)
# Notice each 'new_alien' is a dictionary in the 'alien' list
for alien_spawner in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# Display the first 5 aliens in the fleet using a slice
count = 1
for alien in aliens[:5]:
    print(f"{count} {alien.get('color')} alien! HA HA HA...")
    count = count + 1
print("...")

# Display total count of aliens
print(f"\nThat's a total of {len(aliens)} aliens you're dealing with!")

# We might also use a slice to change some of the dictionaries (aliens)
print("\n(TURN 2) Aliens in range:")
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] ='yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens:
    print(alien['color'])

# Then again at a later run...
print("\n(TURN 3) Aliens in range:")
for alien in aliens[0:5]:
        if alien['color'] == 'green':
            alien['color'] ='yellow'
            alien['points'] = 10
            alien['speed'] = 'medium'
        elif alien['color'] == 'yellow':
            alien['color'] ='red'
            alien['points'] = 15
            alien['speed'] = 'fast'
for alien in aliens:
    print(alien['color'])
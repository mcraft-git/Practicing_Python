
# a 'slice' can be used to pull information about a specific part of a list
players = ['federer','nadal','djokovic','williams','sharapova','barty']
players.sort()
print(f'{players}\n')

print('The second through fourth in the list: ')
print(f'{players[1:4]}\n')

print('The first four in the list: ')
print(f'{players[:4]}\n')

print('The remaining two  in the list: ')
print(f'{players[4:]}\n')

print('The last three in the list: ')
print(players[-3:])

# a slice can be used in a loop as well
print('\nHere are the players for our mixed doubles match: ')
for partners in players[2:]:
    print(partners.title())


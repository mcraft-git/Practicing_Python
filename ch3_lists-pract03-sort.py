# sorting a list permanently (alphabetical order)
cars = ['bmw', 'toyota', 'audi', 'subaru']
cars.sort()
print(cars)

# sorting a list in reverse order permanently
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily (to display what it would look like without changing order)
cars = ['bmw', 'toyota', 'audi', 'subaru']
print(f'Here is the original list: {cars}')
print(f'Here is the sorted list: {(sorted(cars))}')
print(f'Here is the list sorted in reverse: {(sorted(cars, reverse=True))}')
print(f'Here is the original list again: {cars}')

# reverse-sorting the order if items in a list (non-alphabetical)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# displaying the number of items in a list
print(len(cars))
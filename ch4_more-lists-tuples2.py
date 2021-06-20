
# more fun with tuples
print('Original dimensions:')
dimensions = (200,50,100)
for d in dimensions:
    print(d)

# the variable a tuple is assigned to can be overwritten
dimensions = (250,100,150)
print('\nNew dimensions:')
for d in dimensions:
    print(d)

# tuples can be strings too
print('\nFavorite fishies:')
fish = ('trout','bass','brim','catfish')
for f in fish:
    print(f.title())

# chap4 exercises

# use a FOR loop to print the numbers from 1 to 20, inclusive
list1 = list(range(1,21))
for value in list1:
    print(f'\n{value}')

# use the third argument of the range function to make a list of the odd numbers from 1 to 20 and print
list2 = list(range(1,21,2))
for value in list2:
    print(f'\n{value}')
print('If we start with 1 and step by 2, we get the odd numbers.\n')

# ... then do evens
list3 = list(range(2,21,2))
for value in list3:
    print(f'\n{value}')
print('If we start with 2 and step by 2, we get the evens.\n')

# make a list of the multiples of 3 from 3 to 30. Use a FOR loop to print
list4 = list(range(3,31))
for value in list4:
    multiple3 = value*3
    print(f'\n{multiple3}')

# make a list of the cubes of the integers from 1-10
list5 = list(range(1,11))
print('\nList of the first 10 cubes in decimal math:\n')
for value in list5:
    cubes = value**3
    print(f'\n{cubes}')

# now do the same thing as a list comprehension
list6 = [value**3 for value in range(1,11)]
print(f'\n{list6}')
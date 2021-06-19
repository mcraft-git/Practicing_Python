
# this code uses a loop to print the square of each number in a range
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# this code does the same thing using less lines
squares2 = []
for value in range(1,11):
    squares2.append(value ** 2)
print(squares2)

# you can use functions to query information about items in a list
print('\n')
digits = list(range(1,11))

print(f'{min(digits)}\n')
print(f'{max(digits)}\n')
print(f'{sum(digits)}\n')

# a 'List Comprehension' combines a FOR loop and the creation of new elements into one line
squares3 = [value**2 for value in range(1,11)]
print(squares3)
print(f'\n{sum(squares3)}')
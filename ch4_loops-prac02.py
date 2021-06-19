
# this code will display only numbers 1-4, because it will stop at the second number
for value in range(1, 5):
    print(value)
print("\n")

# to display all the numbers that you want, the second number should be +1 beyond the last number in the desired range
for value in range(1, 6):
    print(value)
print("\n")

# only passing one argument to range() will start the sequence at 0
for value in range(6):
    print(value)

# you can convert the results of range() into a list of numbers using the list() function...
# ...wrapping a list around a call to the range() function 
numbers = list(range(1,6))
print(f'\n{numbers}')

# a third argument can be passed to range() as a step sizer...
# ...in this code, the third argument ('2') tells python to skip odd numbers when building a list
int_evens_only = list(range(2,11,2))
print(f'\n{int_evens_only}')
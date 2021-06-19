
# loops follow instructions after a colon, and are often used to process items in a list
magicians = ['alice', 'david', 'carolina']

# "assign [NEW VARIABLE], to every element in [LIST] ...""
# "... and print that element each time you do"
for magician in magicians:
    print(magician)
print("\n")

# each indented line in a loop is executed for each item in the list
pizzas = ['hawaiian', 'supreme', 'four cheese', 'pepperoni']
for pizza in pizzas:
    print(f'I like {pizza} pizza!')
print(f'\nFor breakfast, lunch and din-din, any of these pizzas will do.\n')

# lists are ideal for storing sets of numbers in python
int_primes = [2, 3, 5, 7, 11]

for prime in int_primes:
    print(f'{prime} is a prime number.\n{prime} has only two factors: 1 and itself.\n')
print('Prime numbers are grand! ...But a grand is not a prime.')

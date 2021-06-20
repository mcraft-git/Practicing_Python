
# a tuple is an immutable (unchangeable) list that uses a comma and parenthesis instead of a colon and brackets
dimensions = (200,50)
for d in dimensions:
    print(d)

# tuples can have just one element
my_t = (3,)

# this line will return an error message (because a tuple cant be changed once defined)
dimensions[0] = 250
# creating a list
bicycles = ['trek','canondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list (by index#)
print(bicycles[0])
print(bicycles[2].title())

# access the last item in a list using the index# OR '[-1]' (working backwards from the end; so '[-2]' is second from last)
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-3])

# inserting an item from a list into a string
message = f"My first bicycle was a {bicycles[1].title()}."

print(message)


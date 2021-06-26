
# back to the pizza parlor!
requested_toppings = ['pepperoni','green peppers','mushroom','cheese']

# IF statements used with just the name of a list return a boolean...
# ...TRUE if not empty...
if requested_toppings:

    available_toppings = []
    
    for topping in requested_toppings:
    
        if topping == 'green peppers':
            print(f'Sorry, we ran out of {topping}.')
    
        else:
            print(f'Adding {topping} to your pizza.')
    
            available_toppings.append(topping)
    
    print(f'Your {available_toppings.pop()}, {available_toppings.pop()} and {available_toppings.pop()} pizza is ready!')

#...FALSE if empty
else:

    print('Are you sure you want just a plain pizza?')

print('\nNext order:\n')

# now we re-initialize the list as an empty list
requested_toppings = []

if requested_toppings:
    available_toppings = [] 
    for topping in requested_toppings:   
        if topping == 'green peppers':
            print(f'Sorry, we ran out of {topping}.')   
        else:
            print(f'Adding {topping} to your pizza.')   
            available_toppings.append(topping)    
    print(f'Your {available_toppings.pop()}, {available_toppings.pop()} and {available_toppings.pop()} pizza is ready!')
else:
    print('Are you sure you want just a plain pizza?')
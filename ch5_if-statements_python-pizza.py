
# here's another example of a pizza program (hungry yet?)
# let's use a tuple because these are fixed menu items that wont change
available_toppings = ('pepperroni','sausage','bacon','pineapple','extra cheese','mushroom', 'black olives')

print('Welcome to Python Pizza! Choose up to three toppings for your pizza from our menu.\n')

requested_toppings =['bacon','pineapple','fish chips','extra cheese','mushroom']

if requested_toppings:

    fin_toppings = []
    for topping in requested_toppings:
        if topping in available_toppings:
            fin_toppings.append(topping)
            print(f'Adding {topping} to your pizza')
        else:
            print(f"We don't have {topping}, and NEVER will.")
    print('\n')

    if (len(fin_toppings)) == 3:
        print(f'Your {fin_toppings.pop()}, {fin_toppings.pop()} and {fin_toppings.pop()} pizza is ready!')
    elif (len(fin_toppings)) == 2:
        print(f'Your {fin_toppings.pop()} and {fin_toppings.pop()} pizza is ready!')
    elif (len(fin_toppings)) == 1:
        print(f'Your {fin_toppings.pop()} pizza is ready!')
    else:
        print("That's too many toppings, bucko.")
        adj_fin_toppings = fin_toppings[:3]
        print(f'Your {adj_fin_toppings.pop()}, {adj_fin_toppings.pop()} and {adj_fin_toppings.pop()} pizza is ready!')

else:
    print('Are you SURE you want a plain pizza? I mean, cmon... live a little!')
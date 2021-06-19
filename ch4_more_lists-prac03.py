# chap4 exercise

# making separate list copies
myfavpizza = ['supreme','pepperoni','sausage','cheese']
friendsfavpizza = myfavpizza[:]
print(f'My favorite pizzas: {myfavpizza}\n')
print(f"My friend's favorite pizzas: {friendsfavpizza}\n")

# adding elements to each separate list
myfavpizza.append('hawaiian')
friendsfavpizza.append('tomato')
print(f'My favorite pizzas (better): {myfavpizza}\n')
print(f"My friend's favorite pizzas (grosser): {friendsfavpizza}\n")

# using slices to display different elements
print(f'My top three: {myfavpizza[:3]}\n')
print(f"Friend's top three: {friendsfavpizza[:3]}\n")
print(f'My friend hates: {myfavpizza[-1:]}\n')
print(f'I hate: {friendsfavpizza[-1:]}\n')

# using a loop to print each element in a list
for pizza in friendsfavpizza[:4] :
    print(f'My friend likes {pizza.title()} pizza.')
print('\n')

for pizza in myfavpizza[3:] :
    print(f'{pizza.title()} pizza tastes great with hot sauce!')
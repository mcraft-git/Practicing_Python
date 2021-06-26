
# the code below uses an IF statement with a loop
# the '==' is an equality operator, and is different than a single '='
cars = ['audi','bmw','subaru','toyota']
for c in cars:
    if c == 'bmw':
        print(c.upper())
    else:
        print(c.title())

# the '!=' operator means 'IF these DO NOT match...'
toppings = ['pepperoni','sausage','mushroom','anchovies','tomato']
print('\n')
for t in toppings:
    if t != 'anchovies':
        print(f'One {t} pizza, hold the anchovies!')
    else:
        print(f'We got an {t} pizza! Go hog wild!')

# '<=', '>=', '<', '>' are all operators used with IF statements
# to combine statements, use keywords 'or' & 'and' 
hands = [15,17,23]
print('\n')
for h in hands:
    if (h < 21) or (h == 21):
        print(f'{h} is a good hand, it rides!')
    else:
        print(f'Whoops! {h} means B U S T E D !')


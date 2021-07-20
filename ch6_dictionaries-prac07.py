# We can have a list inside of a dictionary
pizza ={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
# To break up a long line in a print call,"
#   "end with a quote, then indent and open"
#   "with a quote"
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# Now our poll can support multiple languages!
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    'darlene':['c#','javascript'],
}
for name,languages in favorite_languages.items():
    friends = ['sarah','darlene']
    
    print(f"\n{name.title()}'s favorite language(s) are:")
    for language in languages:
        print(f"\t{language.title()}")
    
    if name in friends:
        print(f"Hey, {name.title()}! I see you like {language.title()}!")


# a slice can be used when you want to create a separate copy of an existing list
myfavfoods = ['pizza', 'pasta','watermelon','oranges']
friendfavfoods = myfavfoods[:]

print(f'{myfavfoods}\n')
print(f'{friendfavfoods}\n')

print('Now to prove these are different lists...\n')
myfavfoods.append('cherries')
friendfavfoods.append('PB&J')
print(f'My fav foods: {myfavfoods}\n')
print(f"My friend's fav foods: {friendfavfoods} ... (gross).\n")

# copying a list without using an empty slice [:] wont create separate lists
myfavfoods2 = ['pizza', 'pasta','watermelon','oranges']
friendfavfoods2 = ['pizza', 'pasta','watermelon','oranges']
myfavfoods2 = friendfavfoods2
myfavfoods2.append('cherries')
friendfavfoods2.append('PB&J')
print("I've got a bad feeling about this...\n")
print(f'My fav foods: {myfavfoods2} ... WHAT NO\n')
print(f"My friend's fav foods: {friendfavfoods2} ... (still gross)\n")
lst_motorcycles = ['honda','yamaha','suzuki']
print(lst_motorcycles)

# changing elements in a list
lst_motorcycles[0] = 'ducati'
print(lst_motorcycles)

# appending items to the end of a list
lst_motorcycles.append('honda')
print(lst_motorcycles)
print("\n")

# adding items to an empty list
lst_motorcycles2 = []
lst_motorcycles2.append('honda')
lst_motorcycles2.append('yamaha')
lst_motorcycles2.append('suzuki')
print(lst_motorcycles2)
print("\n")

# inserting elements into a list
lst_motorcycles2.insert(0, 'ducati')
print(lst_motorcycles2)
print("\n")

# removing items from the list
del lst_motorcycles2[0]
print(lst_motorcycles2)
del lst_motorcycles2[1]
print(lst_motorcycles2)
print("\n")

# popping an element from a list removes it from the end of a list and lets you work with it after
lst_motorcycles3 = ['honda','yamaha','suzuki']
print(lst_motorcycles3)

str_poppedmotorcycle = lst_motorcycles3.pop()
print(lst_motorcycles3)
print(str_poppedmotorcycle)
print("\n")

# example use case of pop method (chronologically ordered list)
lst_motorcycles4 = ['honda', 'yamaha', 'suzuki']
str_lastowned = lst_motorcycles4.pop()
print(f"The last motorcyle the author owned was a {str_lastowned.title()}.")

# popping a specific element from a list by index#
str_favmoto = lst_motorcycles4.pop(1)
print(f"...but her favorite bike was a {str_favmoto.title()}!")

# removing an item from a list by its value (and as a value stored in a variable)
print("\n")
lst_motorcycles5 = ['ducati', 'honda', 'suzuki', 'yamaha']
print(lst_motorcycles5)
lst_motorcycles5.remove('honda')
print(lst_motorcycles5)
str_tooexpensive = 'ducati'
lst_motorcycles5.remove(str_tooexpensive)
print(lst_motorcycles5)
print(f"\nA {str_tooexpensive.title()} is too rich for my blood.")

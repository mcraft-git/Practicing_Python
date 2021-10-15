
from datetime import datetime

# This program will compare two lists, one that is old and one that has been updated.
# It will print what's missing from the old list, as well as what's new.

# First, make sure list items are properly formatted...
# (Remove extra characters, enclose with quotes, separate by commas)
li1 = ["old","list","items","here"]
li2 = ["new","list","items","here"]

# Here we convert the lists into sets,
# then use a Bitwise XOR operation ("^") to compare the sets.
# With XOR, only the differences are saved to the variable "diff" as a set.
diff = set(li1) ^ set(li2)

# This outputs the differences to the terminal for sanity checks.
print(diff)

# Now we convert the set back to a list.
diff = list(diff)

# Next, we create two empty lists,
# one to store old list items missing from the new list,
# and one to store the new list items.
missing_old_raw = []
new_items = []

# We iterate over the old list, comparing each item to the new list,
# and appending missing items to "missing_old_raw".
missing_old_raw = []
for i in li1:
    for ii in li2:
        if i not in li2:
            missing_old_raw.append(i)

print(missing_old_raw)

# Due to the sorting method used above, there will be duplicate items.
# We can copy just the unique items to an empty list, "missing_old_fin". 
missing_old_fin = []
for m in missing_old_raw:
    if m not in missing_old_fin:
        missing_old_fin.append(m)

# Missing old items sanity check.
print(f"\nOld items missing: {missing_old_fin}")

# Next we iterate over the list of differences, appending
# anything that we havent identified as a missing old item to "new_items".
for d in diff:
    if d not in missing_old_fin:
        new_items.append(d)

# New items sanity check.
print(f"New items: {new_items}")

# OPTIONAL: Adding a date to the filename (need to verify leading zeroes for single digit day-mo.)
t = datetime.now()
t = str(t)
t = t[:10]

# Finally, we save our intended file path to a variable...
file_path = (f'C:\\file\\path\\goes\\here\\{t}_list_compare.txt')

# Then we write to the report file (or create one).
with open(file_path, 'w') as file_object:
    file_object.write(f"MISSING FROM OLD LIST: {missing_old_fin}\nNEW LIST ITEMS: {new_items}")

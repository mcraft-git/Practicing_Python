lst_myguestlist = [' ichi ',' ryoko ',' miles ',' alie ',' bubba ']

# cleaning input whitespace
str_guest1 = lst_myguestlist[0]
str_guest2 = lst_myguestlist[1]
str_guest3 = lst_myguestlist[2]
str_guest4 = lst_myguestlist[3]
str_guest5 = lst_myguestlist[4]
str_guest1 = str_guest1.strip()
str_guest2 = str_guest2.strip()
str_guest3 = str_guest3.strip()
str_guest4 = str_guest4.strip()
str_guest5 = str_guest5.strip()

print(f"We hereby do formally invite {str_guest1.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest2.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest3.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest4.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest5.title()} to the Grand Ball.\n")

# popping and item from end of list and issuing a message with the popped item
str_naughty = lst_myguestlist.pop()
str_naughty = str_naughty.strip()
print(f"Unfortunately, due to an unseemly scuffle {str_naughty.title()} wont be able to attend.\n")

# inserting a new item at the last position, then cleaning input
lst_myguestlist.insert(4,' woogi ')
str_guest5 = lst_myguestlist[4]
str_guest5 = str_guest5.strip()

print(f"We hereby do formally invite {str_guest1.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest2.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest3.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest4.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest5.title()} to the Grand Ball.\n")

# inserting elements at specific index#'s in the list
print("We are happy to inform the attendees of the Grand Ball that we've secured a bigger ballroom. Which means more guests!\n")
lst_myguestlist.insert(0, ' yeller ')
lst_myguestlist.insert(3, ' benji ')
lst_myguestlist.insert(7, ' lassie ')
print(lst_myguestlist)
str_newfirstguest = lst_myguestlist[0]
str_newmiddleguest = lst_myguestlist[3]
str_newlastguest = lst_myguestlist[7]
str_newfirstguest = str_newfirstguest.strip()
str_newmiddleguest = str_newmiddleguest.strip()
str_newlastguest = str_newlastguest.strip()

print(f"We hereby do formally invite {str_newfirstguest.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest1.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest2.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_newmiddleguest.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest3.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest4.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_guest5.title()} to the Grand Ball.\n")
print(f"We hereby do formally invite {str_newlastguest.title()} to the Grand Ball.\n")

# popping elements from specific index#'s in the list (remember to decrement target index# by 1 after each pop)
print(f"We've been advised that the current arrangement of guests is ill-suited for the setting of the FELINE Grand Ball (for felines ONLY). Letters are forthcoming.\n")

str_doge1 = lst_myguestlist.pop(0)

print(f"We regret to inform you, dear {str_doge1.title()}, that you are dead, and therefore may not attend the Grand Ball. Try the Dead Ball this Autumn.\n")

str_doge2 = lst_myguestlist.pop(2)

print(f"We regret to inform you, dear {str_doge2.title()}, that your participation in this ruse is highly disappointing. You were our hero. No Ball 4 U.\n")

str_doge3 = lst_myguestlist.pop(5)

print(f"We regret to inform you, dear {str_doge3.title()}, that Timmy has fallen down the well again. Otherwise we would have totally let you in.\n")

for catguest in lst_myguestlist:
    print(f"We hereby do (again) formally invite {catguest} to the (doge-free) Grand Ball.\n")

#print(f"We hereby do (again) formally invite {lst_myguestlist[0]} to the (doge-free) Grand Ball.\n")
#print(f"We hereby do (again) formally invite {lst_myguestlist[1]} to the (doge-free) Grand Ball.\n")
#print(f"We hereby do (again) formally invite {lst_myguestlist[2]} to the (doge-free) Grand Ball.\n")
#print(f"We hereby do (again) formally invite {lst_myguestlist[3]} to the (doge-free) Grand Ball.\n")
#print(f"We hereby do (again) formally invite {lst_myguestlist[4]} to the (doge-free) Grand Ball.\n")

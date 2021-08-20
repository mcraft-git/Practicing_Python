
# The 'continue' statement in a loop will cause a program...
# ...to ignore the rest of the loop and return to the start of the loop.
current_number = 0
while current_number != 10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue

    else:
        print(current_number)
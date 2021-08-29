
# Let's use functions to make a toybuilder program!

# When importing, shorten the module name
# with 'as' to make calls easier.
import ch8_functions_toybuilder_module as tm

print("A new toy is waiting to be born and be your new best friend!\n")
print("But it needs your help figuring out what sort of toy it will be...\n")

toy_type = input("What type of toy is it? (pick a number)"
"\n\t1. Teddy Bear\n\t2. Dress-up Dolly\n\t3. Magic Unicorn\n\t4. Rowdy Robot")

toy_parts_fin = tm.toy_parts(toy_type)

toy_name = input("What is its name?\n")


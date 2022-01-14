
# We can use 'try-except' blocks to manage errors that are reported by 'traceback's.
# For example, dividing by zero creates an exception object called 'ZeroDivision-Error'.
# (The exception is reported by name in a traceback if the code is run unmanaged)

# We can use a 'try' block to handle any exceptions we run into,
# thus managing the error-producing code so it will run traceback-free.
from asyncio.windows_events import NULL
from tkinter import END

# # # # # EXAMPLE # # # # #
#try:
#   print(5/0)
#except ZeroDivisionError:
#   print("Unfortunately, in this universe we can't divide by zero.")
# # # # # # # # # # # # # #


# Let's see some try blocks and exceptions in action...
print("\n***OGRE JOE'S SIMPLE CALCULATOR***\n")
questions = True

while questions:

    print("\nUhhh... human pick one o' these:\n")

    operator_type_raw = input("\t1. Add\n\t2. Subtract\n\t3. Multiply\n\t4. Divide\n\t'q' = Quit\n>")

    if operator_type_raw is not 'q':

        # This try block will attempt to pass user inputs to the int() method.
        try:
                operator_type = int(operator_type_raw)
        # The exception object 'ValueError' is thrown when letter characters are passed.       
        except ValueError:
                print("\nHAH! Dummy human use letters. Have to start over!")
        else:

            if operator_type == 1:
                    
                # More inputs means another try block...
                try:
                    first_int_raw = input("\nWhat human's first number?\n>")
                    first_int = int(first_int_raw)
                    second_int_raw = input("\nWhat human's after-first number?\n>")
                    second_int = int(second_int_raw)
                except ValueError:
                    print("HAH! Dummy human use letters. Have to start over!")
                else:            
                    answer = first_int + second_int
                    print(f"\nAnswer is: {answer}")
                    more_questions = input("Human got more silly questions?! (y/n): ")
                    
                    # If user inputs 'y' we END without setting the flag
                    # that our while loop is checking, sending them through again.
                    if more_questions == "y":
                        END
                    else:
                        questions = False
                        break

            elif operator_type == 2:

                try:
                    first_int_raw = input("\nWhat human's first number?\n>")
                    first_int = int(first_int_raw)
                    second_int_raw = input("\nWhat human's after-first number?\n>")
                    second_int = int(second_int_raw)
                except ValueError:
                    print("HAH! Dummy human use letters. Have to start over!")
                else:            
                    answer = first_int - second_int
                    print(f"\nAnswer is: {answer}")
                    more_questions = input("Human got more silly questions? (y/n): ")
                    if more_questions == "y":
                        END
                    else:
                        questions = False
                        break

            elif operator_type == 3:

                try:
                    first_int_raw = input("\nWhat human's first number?\n>")
                    first_int = int(first_int_raw)
                    second_int_raw = input("\nWhat human's after-first number?\n>")
                    second_int = int(second_int_raw)
                except ValueError:
                    print("HAH! Dummy human use letters. Have to start over!")
                else:            
                    answer = first_int * second_int
                    print(f"\nAnswer is: {answer}")
                    more_questions = input("Human got more silly questions? (y/n): ")
                    if more_questions == "y":
                        END
                    else:
                        questions = False
                        break

            elif operator_type == 4:

                try:
                    first_int_raw = input("\nWhat human's first number?\n>")
                    first_int = int(first_int_raw)
                    second_int_raw = input("\nWhat human's after-first number?\n>")
                    second_int = int(second_int_raw)
                except ValueError:
                    print("HAH! Dummy human use letters. Have to start over!")
                else:
                    try:            
                        answer = first_int / second_int
                    except ZeroDivisionError:
                        print("HARRHARR!! Humans can't cut nothing! Only Ogres can.\n"
                        "Start over!!")
                    else:
                        print(f"\nAnswer is: {answer}")
                        more_questions = input("Human got more silly questions? (y/n): ")
                        if more_questions == "y":
                            END
                        else:
                            questions = False
                            break
            
    else:
        quit()

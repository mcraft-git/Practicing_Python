
import ch11_testing_prac01_module as m

name_incomplete = True

while name_incomplete:

    fn = m.get_fn_input()
    mn = m.get_mn_input()
    ln = m.get_ln_input()

    if mn:
        formatted_name = m.get_formatted_name(fn,ln,mn)
    else:
        formatted_name = m.get_formatted_name(fn,ln)

    if formatted_name:
        print(f"Here's the name:\n\t{formatted_name}")
        name_incomplete == False
        break
    else:
        print("Please try again, this is important to the test!")

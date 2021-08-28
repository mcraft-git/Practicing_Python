
# This function uses a default value for the 'state' parameter.
def give_captial(city, state='NJ'):
    """Gives the capital city and state."""
    capital = "Trenton"
    if state == 'NJ':
        print(f"The capital of {state} is {capital}.")
    else:
        print(f"\nYou claim that the capital of {state} is {city}.")

# Inputs are obtained for an if statement.
capital_prompt = input("Please input a capital city: ")
nj_check = input("Is the state NJ? (y/n): ")

# This condition sends both arguments to the function.
if nj_check == "n":
    state_prompt = input("Please enter the state: ")
    give_captial(capital_prompt, state_prompt)

# This condition sends one argument, relying on the default value.
else:
    give_captial(capital_prompt)
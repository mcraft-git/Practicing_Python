
# The 'input()' function pauses a program and waits...
# ...for user input before saving it to a variable 
message = input("Hey, do you think there's an echo in here? ")
print(message)
message = message.lower()
if message == "no":
    print("You're right, it's probably nothing...")
    quit()
else:
    print("<<< [SECRET UNLOCKED] >>>")

# Strings can be combined with '+='
name_prompt = "Welcome to the **** game!"
name_prompt += "\nBefore you can play you must verify a couple details."
name_prompt += "\nWhat is your first name? "
name = input(name_prompt)

# Numerical comparisons require conversion of input from string to integer
age_prompt = input("What is your age? ")
age_prompt = int(age_prompt)

if age_prompt >= 18:
    print(f"\nHello, {name}. You may play the **** game!")
    token = 2
else:
    print(f"\nSorry, {name}. You are not old enough to play the **** game.")
    token = 3

# Modulus operator is "%"
if token % 2 == 0:
    game_prompt = "Can you guess the N A M E of the G A M E ?"
    game_prompt += "\nInput a letter each round to find the answer..."
    game_prompt += "\nAfter four incorrect guesses you will lose. Good luck!"
    print(game_prompt)

    wrong_count = 0
    correct_count = 0
    name_display = ["_","_","_","_"]
    
    while (correct_count < 4) and (wrong_count < 4):
        guess = input("\nTake a guess: ")

        if guess.upper() == "L":
            correct_count += 1
            name_display[0] = guess.upper()
            print(f"\n{name_display} \nYep!")
        elif guess.upper() == "A":
            correct_count += 1
            name_display[1] = guess.upper()
            print(f"\n{name_display} \nYep!")
        elif guess.upper() == "M":
            correct_count += 1
            name_display[2] = guess.upper()
            print(f"\n{name_display} \nYep!")
        elif guess.upper() == "E":
            correct_count += 1
            name_display[3] = guess.upper()
            print(f"\n{name_display} \nYep!")
        else:
            wrong_count += 1
            print(f"\n{name_display} \nNope...")
   
    if wrong_count > 3:
        print("Oh no! You're not **** enough. Maybe try again?")

    else:
        print(f"\nYou did it, {name}! You're totally {name_display}!")

else:
    print(f"\nDon't worry. You have better things to do! (Trust me...)")
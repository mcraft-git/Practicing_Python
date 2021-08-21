
# Let's practice inputs with dictionaries and loops!
responses = {}
polling_active = True

print("\n~ ~ ~ Welcome to the Mandatory Anime Poll! ~ ~ ~")

# Loop will continue while 'polling active' is 'True'
while polling_active:

    name = input("\nWhat is your name?\n")
    name = name.lower()
    anime = input(f"\nHello, {name.title()}. What is the best anime?\n")
    anime = anime.lower()

    # Save each input response as a dictionary key(name) + value(anime)
    # (Will overwrite if input keys are equal)
    responses[name] = anime

    repeat = input("\nThank you. Is there anyone else who needs to answer? (yes/no)\n")

    # Exit loop if input is "no"
    if repeat.lower() == "no":
        polling_active = False

# Check 'responses' dictionary items against if statements
for name, anime in responses.items():
    print(f"\n{name.title()}'s favorite anime is {anime.title()}.")

    if anime != "cowboy bebop":
        print(f"\t{name.title()} is wrong and they must FACE BLOODSHED.")
    else:
        print(f"\t{name.title()} knows what's up. Good job, {name.title()}!!")

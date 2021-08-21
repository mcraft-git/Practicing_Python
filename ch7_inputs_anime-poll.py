

responses = {}
name_bank = []
polling_active = True

print("\n~ ~ ~ Welcome to the Mandatory Anime Poll! ~ ~ ~")
while polling_active:

    name = input("\nWhat is your name?\n")
    name = name.lower()
    anime = input(f"\nHello, {name.title()}. What is the best anime?\n")
    anime = anime.lower()

    responses[name] = anime

    repeat = input("\nThank you. Is there anyone else who needs to answer? (yes/no)\n")

    if repeat.lower() == "no":
        polling_active = False

for name in responses:

    if name in name_bank:
        print(f"\nNice try, {name.title()}. There can be only one BEST ANIME.")
        responses.pop(name)
    else:
        name_bank.append(name)

for name, anime in responses.items():
    print(f"\n{name.title()}'s favorite anime is {anime.title()}.")

    if anime != "cowboy bebop":
        print(f"\t{name.title()} is wrong and they must FACE BLOODSHED.")
    else:
        print(f"\t{name.title()} knows what's up. Good job, {name.title()}!!")

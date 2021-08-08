
# We can use a while loop to check inputs
# Just ask Mr. Crackers!
parrot = "\n*SQUAWK!*"
parrot += "\nCopy till you get crackers. *SQUAWK!*\n"
keyphrase = "crackers"
human = ""

while human.lower() != keyphrase:
    human = input(parrot)
    if human.lower() != keyphrase:
        print(f"*SQUAWK! {human}")
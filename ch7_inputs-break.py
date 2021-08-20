
# The 'break' statement can be used during a loop to stop a program's execution
prompt = "\nPlease enter the name of a city you've visited."
prompt += "\nEnter 'quit' to exit program: "

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"\nI'd love to visit {city.title()}!")
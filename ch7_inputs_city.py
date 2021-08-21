
# Let's learn more about loops!
prompt = "\nPlease enter the name of a city you have visited..."
prompt += "\n...or enter 'quit' to end program: "

# The counter variable must be kept outside of the loop...
# or else the 'continue' statement will re-initialize it to 0
city_count = 0

# The 'while True' statement will cause a loop to run...
# ...until a 'break' statement is reached
while True:

    message = input(prompt)

    # The 'break' statement will exit the loop
    # (To end this program after 3 cities, the count needs to be set at 2)
    # (This is because of the continue statement at the end)
    if city_count == 2:
        print(f"\nI'd love to visit {message.title()}!")        
        print("\nThank you for sharing! :)")
        break

    elif message == "quit":
        break

    # The 'continue' statement will restart the loop
    else:
        print(f"\nI'd love to visit {message.title()}!")
        city_count += 1
        continue

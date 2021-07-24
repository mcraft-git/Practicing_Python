
# We can nest dictionaries inside of dictionaries
# For example, to store user information for a website

users = {
    "foxtrot":{
        'firstname': "Fael",
        'lastname': "Die'Krier",
        'location': "Lakeside Colony",
    },
    "delta":{
        'firstname': "Drave",
        'lastname': "Warrell",
        'location': "Valley of Ruin",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # Here we combine two user_info items into a string
    # And save them to 'full_name' variable
    full_name = f"{user_info['firstname']} {user_info['lastname']}"
    # No combination needed for 'location' variable, so no string
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
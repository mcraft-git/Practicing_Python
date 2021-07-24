
# Ex- Dictionaries in a list
pets = [
    {'pet_name':"Ichi",'animal_type': "Tabby cat", 'guardian_name': "Ana"},
    {'pet_name':"Ryuko",'animal_type': "Shorthair cat", 'guardian_name': "Sabrina"},
    {'pet_name':"Angel",'animal_type': "Welsh terrier", 'guardian_name': "Cody"},
    {'pet_name':"Bindi",'animal_type': "Aligator", 'guardian_name': "Steve"},
]
for pet in pets:
    print(f"\n{pet.get('pet_name')}'s details:")
    print(f"\tClassification: {pet.get('animal_type')}")
    print(f"\tHuman guardian: {pet.get('guardian_name')}")


# Ex- Lists in a dictionary
favorite_places = {
    "Lexie": ["home","mall"],
    "Alex": ["beach","forest","festival"],
    "Michael": ["forest","garden"],
}
for people, places in favorite_places.items():
    print(f"\n{people.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")


# Ex- Dictionaries in a dictionary
cities = {
    
    "philadelphia": {
        "country": "north america",
        "population": 1500000,
        "fact": "Philadelphia is home to America's first hospital and medical school.",
    },
    "stockholm": {
        "country": "sweden",
        "population": 975000,
        "fact": "Stockholm is home to the world's first open-air museum.",
    },
    "sydney": {
        "country": "australia",
        "population": 5000000,
        "fact": "Sydney is the first major city in the world to see the New Year."
    },
}
for city, city_info in cities.items():
    print(f"\nHere are some facts about {city.title()}:")
    
    country = city_info["country"]
    population = city_info["population"]
    fact = city_info["fact"]
    
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")

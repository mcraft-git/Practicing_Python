# How to parse JSON with Python

import json

# From a given string...
jsonstr = """{"People":[{"Id":"1","FirstName":"Jane","LastName":"Doe","Email":"j.doe@names.com","Active":true},     {"Id":"2","FirstName":"John","LastName":"Smith","Email":"j.smith@names.com","Active":true},{"Id":"3",   "FirstName":"Diamond","LastName":"Jim","Email":"d.jim@names.com","Active":false}]}"""

# We use the 'json.loads' function to save a string to a variable object
jsonobj = json.loads(jsonstr)

print(jsonobj["People"][2])

# Or we can use 'json.load(open())' to load directly from a JSON file
jsonobj = json.load(open("sample_json.json"))

print("")
print(jsonobj['People'][2])
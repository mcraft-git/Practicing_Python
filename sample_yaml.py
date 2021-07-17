# This is a Python file that will parse our YAML document to display on the terminal
# First run command "pip3 install pyyaml" from the terminal

import yaml
from yaml import load, load_all

stream = open('sample_yaml.yml','r')
data = load_all(stream, Loader=yaml.FullLoader)

# Below is a more complex parse

#for doc in data:
#    print("New Document:")
#    for key, value in doc.items():
#        print(key + ": " + str(value))
#        if type(value) is list:
#           print(str(len(value)))

# Here is a simpler parse
print("")
for doc in data:
    print(type(doc))
    if type(doc) is dict:
        try:
            print(doc["people"][2])
        except:
            print(doc)
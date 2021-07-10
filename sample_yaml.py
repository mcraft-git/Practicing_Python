# This is a Python file that will stream our YAML document to display on the terminal
# First run command "pip3 install pyyaml" from the terminal

import yaml
from yaml import load, load_all

stream = open('sample_yaml.yml','r')
data = load_all(stream, Loader=yaml.FullLoader)

for doc in data:
    print("New Document:")
    for key, value in doc.items():
        print(key + ": " + str(value))
        if type(value) is list:
            print(str(len(value)))
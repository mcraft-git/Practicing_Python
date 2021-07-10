# This is how to parse XML with Python

# Here's how to import the XML ElementTree library
#import xml.etree.ElementTree as ET

# Here's how to import the lxml extension (which is better for parsing XML)
from lxml import etree as ET


# Get the XML file data
stream = open('sample_xml.xml','r')

# Parse the data into an ElementTree object
xml = ET.parse(stream)

# Get the 'root' Element object from the ElementTree
root = xml.getroot()

# Iterate through each child of the root Element
for e in root:
    # Print the stringified version of the Element
    print(ET.tostring(e))
    print("")

    # Print the 'Id' attribute of the Element object
    print(e.get("Id"))


# Alternatively, 'xmltodict' can be used
print("")
import xmltodict

stream = open('sample_xml.xml', 'r')

# Parse the XML file into an 'OrderedDict'
xml = xmltodict.parse(stream.read())

# print items from the OrderedDict
for e in xml["People"]["Person"]:
    print(e)
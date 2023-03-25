from pyzotero import zotero
import ZoteroPdf
import configparser

# Get username and password from .ini file
config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('login', 'username')
password = config.get('login', 'password')

# Create Zotero object
zot = zotero.Zotero(username, 'user', password)
zpdf = ZoteroPdf.ZoteroPdf(zot)

# Set collection name you want to get
collection_name = 'Modern Object Detectors'

# Build dictionary with item title as key and item text as value
""" item_dict = zpdf.build_text_dict(collection_name)

# Get first item in the dictionary
item = list(item_dict.items())[0]
print(item) """

# Build dictionary with item title as key and item URL as value
item_dict = zpdf.build_url_dict(collection_name)

# Print every item in the dictionary line by line
for item in item_dict:
    print(item)
    print(item_dict[item])
    print()












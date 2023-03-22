from pyzotero import zotero

import utils

# Get ID and API KEY from: https://www.zotero.org/settings/keys
# ID: 11367674
# API KEY: J7AUgsFVqkr6isX4DgpSmu3N

# Test with curl
# curl -X GET "https://api.zotero.org/users/Emanuele1997/items?format=json" -H "Zotero-API-Key: J7AUgsFVqkr6isX4DgpSmu3N"

zot = zotero.Zotero('11367674', 'user', 'J7AUgsFVqkr6isX4DgpSmu3N')

# Set collection name you want to get
collection_name = 'Breast Cancer'

# Retrieve a list of top-level collections
collections = zot.collections_top()

# Loop through the collections and search for the desired collection name to get the collection ID
for collection in collections:
    if collection['data']['name'] == collection_name:
        collection_id = collection['data']['key']
        break

# Print the collection ID
print(f"The ID for the {collection_name} collection is {collection_id}.")

# Get all items from the collection
items = zot.everything(zot.collection_items(collection_id))

print(items)

# Get pdf of each item
for item in items:
    # Get item key
    item_key = item['key']
    print(item_key)

    # Get pdf url
    pdf_url = utils.get_pdf_url(item_key, zot)

    # Get pdf text
    #pdf_text = utils.get_pdf_text(pdf_url)

""" # Get article by title
item = zot.top(q = 'Attention Is All You Need')

# Get item key
item_key = item[0]['key']
print(item_key)

# Get pdf url
pdf_url = utils.get_pdf_url(item_key, zot)

# Get pdf text
pdf_text = utils.get_pdf_text(pdf_url) """






from pyzotero import zotero
import PyPDF2
import urllib.request
import io

# Get ID and API KEY from: https://www.zotero.org/settings/keys
# ID: 11367674
# API KEY: J7AUgsFVqkr6isX4DgpSmu3N

# Test with curl
# curl -X GET "https://api.zotero.org/users/Emanuele1997/items?format=json" -H "Zotero-API-Key: zhBa7zwPcbyd5rIBmF83A4SN"

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

# Print the items
for item in items:
    print(item['data']['title'])

#get text from pdf title
pdf_link = items[1]['links']['alternate']['href']
pdf_link = 'https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-7580.2005.00417.x'
# Download the PDF file from the URL insert as input
print(pdf_link)
req = urllib.request.Request(pdf_link, headers={"User-Agent": "Chrome"})
remote_file = urllib.request.urlopen(req).read()
remote_file_bytes = io.BytesIO(remote_file)
pdfdoc_remote = PyPDF2.PdfReader(remote_file_bytes)
# Extract the text from the PDF file
pdf_text = ""
for i in range(len(pdfdoc_remote.pages)):
    print("Loading page:", i)
    page = pdfdoc_remote.pages[i]
    page_content = page.extract_text()
    pdf_text += page_content
print(pdf_text)

""" # Try to get text from pdf for each item
for item in items:
    try:
        # Get the pdf link for the item
        pdf_link = item['links']['alternate']['href']
        # Download the PDF file from the URL insert as input
        print(pdf_link)
        req = urllib.request.Request(pdf_link, headers={"User-Agent": "Chrome"})
        remote_file = urllib.request.urlopen(req).read()
        remote_file_bytes = io.BytesIO(remote_file)
        pdfdoc_remote = PyPDF2.PdfReader(remote_file_bytes)
        # Extract the text from the PDF file
        pdf_text = ""
        for i in range(len(pdfdoc_remote.pages)):
            print("Loading page:", i)
            page = pdfdoc_remote.pages[i]
            page_content = page.extract_text()
            pdf_text += page_content
        print(pdf_text)
    except:
        print("No pdf") """









""" # Get all items
items = zot.everything(zot.top())

# Get all items from a specific collection
items = zot.everything(zot.collection_items('3Q2Q2Q2Q'))

# Get all items from a specific tag
items = zot.everything(zot.tag_items('python'))

# Get all items from a specific search
items = zot.everything(zot.search('python'))

# Get all items from a specific item type
items = zot.everything(zot.item_type('book'))

# Get all items from a specific item type and collection
items = zot.everything(zot.item_type('book', '3Q2Q2Q2Q'))

# Get all items from a specific item type and tag
items = zot.everything(zot.item_type('book', tag='python')) """



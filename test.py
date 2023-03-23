from pyzotero import zotero
import ZoteroPdf

# Get ID and API KEY from: https://www.zotero.org/settings/keys
# ID: 11367674
# API KEY: J7AUgsFVqkr6isX4DgpSmu3N

# Test with curl
# curl -X GET "https://api.zotero.org/users/Emanuele1997/items?format=json" -H "Zotero-API-Key: J7AUgsFVqkr6isX4DgpSmu3N"

zot = zotero.Zotero('11367674', 'user', 'J7AUgsFVqkr6isX4DgpSmu3N')

zpdf = ZoteroPdf.ZoteroPdf(zot)

# Set collection name you want to get
collection_name = 'Modern Object Detectors'

# Build dictionary with item title as key and item text as value
item_dict = zpdf.build_dict(collection_name)











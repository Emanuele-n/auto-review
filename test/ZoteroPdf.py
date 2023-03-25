import PyPDF2
import urllib.request
import io

class ZoteroPdf:
    def __init__(self, zot):
        self.zot = zot

    def build_text_dict(self, collection_name):
        # init dictionary with item title as key and item text as value (maybe is better to use the key as key...)
        item_dict = {}

        # Get collection ID
        collection_id = self.get_collection_id(collection_name)

        # Get all items from the collection
        items = self.zot.everything(self.zot.collection_items(collection_id))

        # Counter to check how many items are being checked
        counter = 0
        for item in items:

            # Get item title and key
            item_title = self.traverse_dict(item, key_desired='title')
            #item_key = item['key']

            # Find item url to pdf
            try:        
                print(f"\nChecking item {items.index(item) + 1} out of {len(items)}.", "Title:", item_title)
                item_url = self.traverse_dict(item, key_desired='url')
                print("url:", item_url)
            except:
                print(f"Error: {item_title} has no url\n")
                continue

            # Get pdf text
            if item_url != None:
                # Check if it is not empty
                if len(item_url) > 2:
                    try:
                        pdf_text = self.get_pdf_text(item_url)
                        counter += 1
                    except:
                        print(f"Error: Cannot download {item_title} from the url provided\n")
                        continue
                else:
                    print(f"Error: {item_title} has empty url\n")
                    continue
                
                # Add item title and text to dictionary
                item_dict[item_title] = pdf_text

        # Print number of items checked
        print(f"\Retrieved {counter} items.\n")
        print(item_dict)
        return item_dict

    def build_url_dict(self, collection_name):
        # init dictionary with item title as key and item text as value (maybe is better to use the key as key...)
        item_dict = {}

        # Get collection ID
        collection_id = self.get_collection_id(collection_name)

        # Get all items from the collection
        items = self.zot.everything(self.zot.collection_items(collection_id))

        # Counter to check how many items are being checked
        counter = 0
        for item in items:

            # Get item title and key
            item_title = self.traverse_dict(item, key_desired='title')
            #item_key = item['key']

            # Find item url to pdf
            try:        
                print(f"\nChecking item {items.index(item) + 1} out of {len(items)}.", "Title:", item_title)
                item_url = self.traverse_dict(item, key_desired='url')
                print("url:", item_url)
            except:
                print(f"Error: {item_title} has no url\n")
                continue

            # Add item title and text to dictionary
            if item_url != None and len(item_url) > 2:
                counter += 1
                item_dict[item_title] = item_url

        # Print number of items checked
        print(f"\Retrieved {counter} items.\n")
        print(item_dict)
        return item_dict

    def get_publication_year(self, item):
        # Get publication year
        print(item)
        try:
            publication_year = self.traverse_dict(item, key_desired='date')
            publication_year = publication_year.split("-")[0]
        except:
            publication_year = None
        return publication_year

    def get_collection_id(self, collection_name):
        # Retrieve a list of top-level collections
        collections = self.zot.collections()

        # Loop through the collections and search for the desired collection name to get the collection ID
        for collection in collections:
            if collection['data']['name'] == collection_name:
                collection_id = collection['data']['key']
                break

        # Print the collection ID
        print(f"The ID for the {collection_name} collection is {collection_id}.")

        return collection_id
        
    def get_pdf_text(self, pdf_url):
        # Download the PDF file from the URL insert as input
        req = urllib.request.Request(pdf_url, headers={"User-Agent": "Chrome"})
        remote_file = urllib.request.urlopen(req).read()
        remote_file_bytes = io.BytesIO(remote_file)
        pdfdoc_remote = PyPDF2.PdfReader(remote_file_bytes)

        # Extract the text from the PDF file
        pdf_text = ""
        for i in range(len(pdfdoc_remote.pages)):
            #print("Loading page:", i)
            page = pdfdoc_remote.pages[i]
            page_content = page.extract_text()
            pdf_text += page_content
        #print(pdf_text)
        print("PDF text loaded\n")
        return pdf_text

    def traverse_dict(self, dict_obj, key_desired=None):
        # If key == key_desired, return value
        if key_desired:
            for key, value in dict_obj.items():
                if key == key_desired:
                    #print(key, value)
                    return value
                elif isinstance(value, dict):
                    result = self.traverse_dict(value, key_desired)
                    if result is not None:
                        return result
                    
        # If key_desired == None, print all keys and values
        else:
            for key, value in dict_obj.items():
                print(key, value)
                if isinstance(value, dict):
                    self.traverse_dict(value)

        return None
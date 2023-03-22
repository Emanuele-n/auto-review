import PyPDF2
import urllib.request
import io

def get_pdf_url(item_key, zot):
    # An item's attachments
    children = [c for c in zot.children(item_key)]

    # Just get the PDFs
    pdf_data = [c for c in children if c['data'].get('contentType') == 'application/pdf']

    # get pdf with key 'url'
    pdf_url = pdf_data[0]['data']['url']
    print(pdf_url)
    return pdf_url
    
def get_pdf_text(pdf_url):
    # Download the PDF file from the URL insert as input
    req = urllib.request.Request(pdf_url, headers={"User-Agent": "Chrome"})
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
    #print(pdf_text)
    print("PDF text loaded\n")
    return pdf_text

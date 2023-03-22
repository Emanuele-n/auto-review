from transformers import pipeline
import urllib.request
import PyPDF2
import io
import tensorflow as tf

# Check if GPU is available
GPU_name = tf.test.gpu_device_name()
if GPU_name != '/device:GPU:0':
    raise SystemError('GPU device not found')
else:
    device_index = 0
    print('Found GPU at: {}'.format(GPU_name))

# Download the PDF file from the URL insert as input
URL = input("Enter the URL of the PDF file:\n")
#URL = "https://bitcoin.org/bitcoin.pdf"
req = urllib.request.Request(URL, headers={"User-Agent": "Chrome"})
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

# Create a pipeline for question answering
nlp = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2",
    framework='tf', 
    device=device_index
)

while(True):
    # Ask a question
    context = pdf_text
    question = input("Enter your question:\n")

    question_set = {"context": context, "question": question}

    results = nlp(question_set)

    # Print the answer
    print("\nAnswer: " + results["answer"] + "\n")
from transformers import pipeline
import urllib.request
import PyPDF2
import io
import tensorflow as tf
import ZoteroPdf

""" # Check if GPU is available
GPU_name = tf.test.gpu_device_name()
if GPU_name != '/device:GPU:0':
    raise SystemError('GPU device not found')
else:
    device_index = 0
    print('Found GPU at: {}'.format(GPU_name)) """

# Download the PDF file from the URL insert as input
#URL = input("Enter the URL of the PDF file:\n")
URL = "https://bitcoin.org/bitcoin.pdf"
pdf_text = ZoteroPdf.get_pdf_text(URL)

print(pdf_text)

# Create a pipeline for question answering
nlp = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2",
    framework='tf', 
    #device=device_index
)

while(True):
    # Ask a question
    context = pdf_text
    question = input("Enter your question:\n")

    question_set = {"context": context, "question": question}

    results = nlp(question_set)

    # Print the answer
    print("\nAnswer: " + results["answer"] + "\n")
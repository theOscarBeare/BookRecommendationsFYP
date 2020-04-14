'''
    Module to convert given PDF file to txt file
'''
import PyPDF2
import textract
import sys

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def conv_file(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""   #We will store all data here
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    return text


if __name__ == "__main__":
    text_file = open('{}.txt'.format(sys.argv[1]), 'w')
    text_file.write(conv_file(sys.argv[1]))
    text_file.close()
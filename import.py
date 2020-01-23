import PyPDF2
import re
import csv
import http
pdfFileObj=open("50YearsDataScience.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
num_pages=pdfReader.numPages
print(num_pages)
count=0

pdfObj=pdfReader.getPage(0)
text = pdfObj.extractText()
#print("......................................................")
#print(text)

keywords= re.findall(r'[a-zA-Z0-9]\w+',text)
print(len(keywords))
print(keywords)







    

    


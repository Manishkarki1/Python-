import pyttsx3
import pyPDF2
book=open("book.pdf","rb")
pdfreader=pyPDF2.pdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
page=pdfreader.getPage(8)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()

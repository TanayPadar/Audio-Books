#Audio Book by JP 
#Youtube Channel -: https://tinyurl.com/1smu75d8
#Youtube Name -: Junior Programmer 

#Import Modules 
import pyttsx3
import PyPDF2

#Open File to convert
book = open('python_tutorial.pdf','rb') #PDF file location 

#Main Loop
pdfReader=PyPDF2.PdfFileReader(book)
pages =  pdfReader.numPages
print (pages)
speaker = pyttsx3.init()
page= pdfReader.getPage(26)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()

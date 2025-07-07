def pdfHandler():
    print("pdf handler called...")

def txtHandler():
    print("text handler called..")    
def imageHandler():
    print("image handler called...")    



def handleFile(cb):
    print("file handler called..")
    cb()
    

fileName ="abc.pdf"    

if fileName.endswith(".pdf"):
    handleFile(pdfHandler)
elif fileName.endswith(".txt"):
    handleFile(txtHandler)
elif fileName.endswith(".jpg"):
    handleFile(imageHandler)        
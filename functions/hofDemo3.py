def pdfHandler(fileName):
    print("pdf handler called...",fileName)

def txtHandler(fileName):
    print("text handler called..",fileName)    
def imageHandler(fileName):
    print("image handler called...",fileName)    



def handleFile(cb,fileName):
    print("file handler called..")
    cb(fileName)
    

fileName ="abc.txt"    

if fileName.endswith(".pdf"):
    handleFile(pdfHandler,fileName)
elif fileName.endswith(".txt"):
    handleFile(txtHandler,fileName)
elif fileName.endswith(".jpg"):
    handleFile(imageHandler,fileName)        
def pdfHandler(fileName):
    print("pdf handler called...",fileName)
    return f"{fileName} file opened successfully"

def txtHandler(fileName):
    print("text handler called..",fileName)    
    return f"{fileName} file opened successfully"

def imageHandler(fileName):
    print("image handler called...",fileName)    
    return f"{fileName} file opened successfully"



def handleFile(cb,fileName):
    print("file handler called..")
    # x = cb(fileName)
    # print(x)
    return cb(fileName)
    

fileName ="abc.txt"    
ans = None

if fileName.endswith(".pdf"):
    ans = handleFile(pdfHandler,fileName)
elif fileName.endswith(".txt"):
    ans = handleFile(txtHandler,fileName)
elif fileName.endswith(".jpg"):
    ans = handleFile(imageHandler,fileName)        
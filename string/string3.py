name = "ram" #3 0 1 2
revName = ""

for i in range(len(name)-1,-1,-1):
    revName+=name[i]

print(f"rev name = {revName}")    

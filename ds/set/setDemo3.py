mumbai = {"amit","ram","kunal","jay"}
goa = {"amit","kunal","parth","jainil"}
pune = {"amit","rajvi","krishna","priya"}


data = {"class1":["amit","sumit","amit","raj"],"class2":["jay","raj","amit","kunal","jay"]}

x={}

for i,j in data.items():
    x[i] = set(j)

print(x)    
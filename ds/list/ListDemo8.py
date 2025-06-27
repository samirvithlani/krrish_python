#list compr...
#[1,2,3,4,5]

data=[i for i in range(1,6)]

# for i in range(1,6):
#     data.append(i)

print(data)    


users = ["amit","sumit","jay","raj","parth"]
upperuser=[i.upper() for i in users]
print(upperuser)



#10%
sales = [100,200,220,600,777]
aftsales =[i * 0.9 for i in sales]
print(aftsales)



#if 
salesgt500 = [i for i in sales if i>500]
print(salesgt500)


users = ["amit","sumit","jay","raj","parth"]
userlengt3 = [i for i in users if len(i)>3]
print(userlengt3)


numbers = [100,-90,120,89,-1000,98,0]
numlab = ["pos" if i<0 else "neg" for i in numbers]
print(numlab)
numlab = ["pos" if i<0 else ("zero" if i ==0 else "neg") for i in numbers]
print(numlab)


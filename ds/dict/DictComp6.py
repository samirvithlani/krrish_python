#{1:1.}

# x = {i:i**2 for i in range(1,6)}
# print(x)


users = ["Ram","shyam","amit","naman","sumit","raj","bob"]

#x = {i:len(i) for i in users}
x = {i:len(i) for i in users if len(i)>4}
print(x)

x = {i[0]:i for i in users}
print(x)

x = {i:"yes" if i == i[::-1] else "no"for i in users}
print(x)


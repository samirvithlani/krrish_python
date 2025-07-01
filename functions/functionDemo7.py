# def demo():
#     print("demo funciton called...")

# x = demo
# x()

x = lambda : print("demo called....")
x()

# def add(a,b):
#     print(a+b)

# x = lambda a,b:print(a+b)
# x(12,22)

x = lambda a,b : a+b
print(x(100,200))

# findMax = lambda a,b : a if a<b else b
# print(findMax(100,2900))

findmax = lambda a,b,c : a if a>b  else(b if b>c  else c)
print(findmax(10,11,2))
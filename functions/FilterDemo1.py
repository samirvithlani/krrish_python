numbers = [i for i in range(1,101)]

ans = filter(lambda x: x>50 and x & 3==0,numbers)
print(list(ans))


names = ["ram","parth","shyam","ajay","kunal","raj"]

x = map(lambda i: i.upper(),list(filter(lambda x:x.startswith("s"),names)))
print(list(x))
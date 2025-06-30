# x = set({})
# print(x)

x = {10,20,10,101,20,34,56}
print(x)

x.add(1000)
x.update({90,78,67,880})
print(x)
# for i in x:
#     print(i)

removedelm = x.pop()
print(f"removing... {removedelm}")
x.remove(10)
x.discard(101)
print(x)

data = {"India":"New Delhi","China":"Beig","Russia":"Moscow"}
print(data)

print(data["India"])

k = data.keys()
print(list(k))
v = data.values()
print(v)

kv = data.items()
print(kv)

for i,j in data.items():
    print(f"{i} {j}")
data = {"India":"New Delhi","China":"Beig","Russia":"Moscow","China":"Sanghai"}
print(data)
if "China" in data:
    removedValue = data.pop("China")
    print(f"removing..{removedValue}")
else:
    print("no key found....")    


remvedData = data.popitem()
print("remved item",remvedData)
print(data)
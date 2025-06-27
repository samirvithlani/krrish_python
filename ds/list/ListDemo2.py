numbers = [12,22,45,67,8,90,1,2,90,3,4,5,6,7]
#numbers.clear()
print(numbers)
#removedElm = numbers.pop()
removedElm = numbers.pop(2)
print(f"remving...{removedElm}")
print(numbers)

if 905 in numbers:
    numbers.remove(905) #ValueError: list.remove(x): x not in list
else:
    print("no is not found...")    
print(numbers)



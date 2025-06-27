numbers = [12,22,45,67,8,90,1,2,90,3,4,5,6,7]
print(numbers)
#numbers.sort()
numbers.sort(reverse=True)
print(numbers)

users = ["ram","amit","shyam","parth","kunal","ajay","raj","amit",'ram','parth']
print(users)
users.sort(key=len,reverse=True)
print(users)

unique_list =[]
duplicate_elm =[]

for i in users:
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicate_elm.append(i)    

print(unique_list)        
print(duplicate_elm)
users1 = {"ram","seeta","lakshman","krishna"}
users2 = {"ram","arjun","sahdev","krishna"}

#x = users1.union(users2)
#x = users1 | users2
#x = users1.difference(users2)
#x = users2 - users1
#x = users1.intersection(users2)
#x = users1 & users2

#x = users1.symmetric_difference(users2)

x = users1.issuperset(users2)
x= users1.issubset(users2)
print(x)


import functools

marsk = [1,2,3,4,5]

total = functools.reduce(lambda x,y:x+y,marsk)
print(total)


#1st map will return all values
#2nd filter conditin satisifed values
#3rd reduce cumn....
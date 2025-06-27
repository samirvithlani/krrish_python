#7. Word Length Pairs
Input = ["hello", "world", "hi", "python"]
#Output= [("hello", 5), ("world", 5), ("hi", 2), ("python", 6)]

output = [[i,len(i)] for i in Input]
print(output)
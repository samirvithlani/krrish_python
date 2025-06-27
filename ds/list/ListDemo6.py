data = [[10,20,30],[1,2,3],[100,200,300]]
#print(data[0][0])

# for i in range(len(data)):
#     #print(data[i])
#     for j in range(len(data[i])):
#         print(data[i][j],end=" ")
#     print()    



# for i in data:
#     for j in i:
#         print(j,end=" ")
#     print()    
    
   
   
# data= [100,200,300,340]    

#print(f"max = {max(data)}")

# big = data[0]

# for i in data:
#     if i>big:
#         big =i

# print(big)        


score = [["virat",80,90,77],["rohit",78,56,122],["ms",88,7,111]]

#score=[["virat",total],[],[]]

playerName = None
finalscore =[]
ans =0
for i in range(0,len(score)):
    playerName = score[i][0]
    for j in range(1,len(score[i])):
        #print(score[i][j],end=" ")
        ans = ans + score[i][j]
    finalscore.append([playerName,ans])
    ans=0

print(finalscore)    
        
        
    
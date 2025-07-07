
def orderFood(func): #3 func == throwparty
    
    def inner(): #5
        print("ordering food...") #6
        func() #7
    
    
    return inner    #4


@orderFood #2
def throw_party(): #8
    print("throwing party...") #9
    

throw_party() #1   
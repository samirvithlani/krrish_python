def orderfood(func):
    
    def inner(noofperson):
        print(f"no of person = {noofperson}")
        func(noofperson+20)
    
    
    return inner


@orderfood
def throw_party(noofperson):
    print(f"throwing party...{noofperson}")


throw_party(100)    
        
        
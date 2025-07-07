def safediv(func):
    
    def inner(no1,no2):
        if(no2==0):
            return f"can not divide by zero"
        else:
            return func(no1,no2)
    
    return inner


@safediv
def div(no1,no2):
    #print(f"no = {no1/no2}")
    return no1 / no2

x = div(10,0)    
print(x)
    
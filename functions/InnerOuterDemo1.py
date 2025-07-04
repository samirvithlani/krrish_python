# def outer():
#     print("outer function called..")
#     def inner():
#         print("inner function called..")
    
#     inner()    


# outer()    

# def outer():
#     print("outer function called..")
#     def inner():
#         print("inner function called..")
#         return f"inner function returning {1000}"
    
#     inr = inner()    
#     print("inner returnt",inr)


# outer()    

# def outer():
#     print("outer function called..")
#     def inner():
#         print("inner function called..")
#         return f"inner function returning {1000}"
    
#     inr = inner()    
#     print("inner returnt",inr)
#     return f"outer function returning {2000}"


# x = outer()    
# print(x)


# def outer():
#     print("outer function called..")
#     def inner():
#         print("inner function called..")
#         return f"inner function returning {1000}"
    
#     return f"outer function returning {inner()}"


# x = outer()    
# print(x)



# def outer():
#     print("outer function called..")
#     def inner():
#         print("inner function called..")
#         return f"inner function returning {1000}"
    
#     return inner


# x = outer()    
# print(x)
# print(x())



def outer(no1):
    print("outer function called..")
    def inner(no):
        print("inner function called..")
        return f"inner function returning {no}"
    
    return inner


x = outer(199)    
print(x)
print(x(999))
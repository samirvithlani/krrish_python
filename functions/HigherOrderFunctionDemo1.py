
def toBeCalled():
    print("to be called...")

def test(a):
    print("value of a = ",a)
    a()

# test(10)
# test("mm")    
# test(False)
# test([])
test(toBeCalled)
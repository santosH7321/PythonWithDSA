# pass by value 

def addOne(x):
    x = x + 1
    print("Inside function", x)

x = 5
addOne(x)
print("Outside function:", x)
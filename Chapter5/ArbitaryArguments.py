def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

output = addAllNumbers(1,2,3,4,5)
print("The sum is", output)
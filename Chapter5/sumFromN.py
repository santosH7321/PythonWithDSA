def add(n1=0, n2=0):
    print("n1:", n1)
    print("n2:", n2)
    sum = n1 + n2
    return sum

#postition argument
#  print("The sum is", add(2,3))

#keyword argument (named arguments)
#print("The sum is", add(n2=2, n1=3))

#defult arguments
print("The sum is", add(3))
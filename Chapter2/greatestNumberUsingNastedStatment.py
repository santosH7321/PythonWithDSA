n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

# using nasted if else statment
if n1 > n2:
    if n1 > n3:
        print(n1, "Is the greatest element: ")
    else:
        print(n3, "is the greatest element: ")
    if n2 > n3 :
        print(n2, "is the greatest element: ")
    else:
        print(n3 , "is the greatest element: ")
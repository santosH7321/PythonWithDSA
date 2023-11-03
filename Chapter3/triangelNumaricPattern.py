n = int(input("Enter a no: "))

for i in range(1, n+1): # loop for row
    for j in range(1, i+1): # loop for columns
        print(j, end="")
    print()
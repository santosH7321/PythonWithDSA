n = int(input("Enter n: "))
for i in range(1, n+1): #loop for rows
    #printing space
    print(" " * (n-i), end="")

    #priniting digits
    for j in range(1, 2 * i):
        print(j, end="")
    print()


# Enter n: 4
#    1
#   123
#  12345
# 1234567
# Take positive integer input and tell if it is a four digit number or not.

num = int(input("Enter a number: "))

if num >= 1000 and num <= 9999:
    print("it is four digit number: ", num)
else:
    print("Not a 4 digit Number: " ,num)
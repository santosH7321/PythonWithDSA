num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

# if number one is greatest 
if num1 > num2 and num1 > num3 :
    print("Number One is greater: ",num1)
# if number two is greatest
elif num2 > num3 and num2 > num1:
    print("Number two is greater: ",num2)
# if number three is greatest number
else:
    print("Number three is greater: ",num3)
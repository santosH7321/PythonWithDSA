num = int(input("Enter a positive number: "))

#checking whether it is divisible by 15

if num % 15 == 0 :
    print("Number is divisible by 15: ")
else:
    #checking if divisible by 3 or 5
    if num % 3 == 0 and num % 5 == 0 :
        print("Number is not divisible by 15 but divisible by 3 or 5")
    else:
        print("Number is neither divisible by 3 nor by 5")
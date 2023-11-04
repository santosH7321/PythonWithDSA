input_string = input("Enter string: ")
n = int(input("Enter n: "))

#creating dictionary for mirror operation
alphabetes = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabates = alphabetes[::-1]
dict1 = dict(zip(alphabetes,reverse_alphabates))

#finding the part of strig on which we will do mirror operation
prefix = input_string[0:n-1]
sufix = input_string[n-1:]

#inding the mirror string
mirror = ""
for i in range(0, len(sufix)):
    mirror = mirror + dict1[sufix[i]]

#creating the final string
res = prefix + mirror
print("The result is: ", res)
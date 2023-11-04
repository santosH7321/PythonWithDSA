fruits = ["Apple", "Mango", "Cherry", "Banana"] # creat a list

print(fruits) # print a list

# print(type(fruits)) # check type of list

# print(len(fruits)) # check length of list

# # checking if an item is present in the

# if "Banana" in fruits:
#     print("Banana is part of the list")

# #checking if an itwm is not present in the list

# if "Kiwi" not in fruits:
#     print("Kiwi is not part of the list")

# Indexing in list
# print(fruits[1]) # mango
# print(fruits[-3]) # mango

# print(fruits[1:3]) #['Mango', 'Cherry']
# print(fruits[-3:-1])  #['Mango', 'Charry']

# fruits.append("kiwi")

# print(fruits)

# fruits.insert(2, "kiwi")
# print(fruits)

# more_fruits = ["kiwi", "papaya"]
# fruits.extend(more_fruits)
# print(fruits)


# fruits.remove("Banana")
# print(fruits)

# fruits.pop()
# print(fruits)

#changing and updating item in a list
# fruits[1] = "kiwi"
# print(fruits)

# fruits[1:3] = ["papaya"]
# print(fruits)

#Shorting a list

# fruits.sort() # This is by defult assending order
# print(fruits)

# fruits.sort(reverse=True) #descending
# print(fruits)

# reverse
# fruits.reverse()
# print(fruits)

# new_fruits = [fruits for fruits in fruits if "a" in fruits ]
# print(new_fruits)

# copy a list
# new_fruits = fruits.copy()
# print(new_fruits)

# new_fruits = fruits + new_fruits
# print(new_fruits)

# Nasted list
# fruits.insert(2, ["kiwi", "papaya"])
# print(fruits)
# print(fruits[2][0])

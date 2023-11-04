# Reverse a tuple.
# input: tuples = ('z','a','d','f','g','e','e','k')
# Output: ('k','e','e','g','f','d','a','z')

# input: tuples = (10,11,12,13,14,15)
# Output: (15,14,13,12,11,10)

input_tuple = (1,2,3,4,5,6)

list = []

# adding reversed values in a list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)  #type cast into tuple
print(output_tuple)
# Examples:
# input: List = [23,65,19,90], idx2=2
# Output: [19,65,23,90]
# input: List = [1,2,3,4,5], idex1 = 1, idx2 = 4
# Output: [1,5,3,4,2]

n = int(input("Enter size of list: "))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index1: "))
idx2 = int(input("Enter index2: "))
# swapping values at idx1 and idx2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)
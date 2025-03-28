# Brute_Force
import array as arr
a = arr.array('i', [1, 1, 0, 1 , 0, 7, 0, 7, 7, 0])
n = len(a)
temp = arr.array('i', [])
for i in range(0, n):
    if a[i] != 0:
        temp.append(a[i])
x = len(temp)
for i in range(0, x):
    a[i] = temp[i]
for i in range(x, n):
    a[i] = 0
print(a)

# Optimal_Approach
nums = arr.array('i', [1, 0, 7, 8, 0 , 0, 7, 0])
j = -1
for i in range(0, len(nums)):
    if nums[i] == 0:
        j = i
        break
if j != -1:
    for i in range(j+1, len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1
print(nums)
print(j)
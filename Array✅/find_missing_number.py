# Brute_Force
lst = [1, 2, 4, 5]
n = 5
for i in range(1, n+1):
    flag = 0
    for j in range(0, n-1):
        if lst[j] == i:
            flag = 1
            break
    if flag == 0:
        print(i)

# Better_Approach
lst = [1, 2, 4, 5]
n = len(lst) + 1
hash_array = [0] * (n+1)
for i in lst:
    hash_array[i] += 1
for i in range(1, len(hash_array)):
    if hash_array[i] == 0:
        print(i)
        break

# Optimal_Approach
nums = [1, 2, 4, 0]
n = len(nums)
sum_n = n * (n + 1) // 2
sum_lst = 0
for i in nums:
    sum_lst += i
missing_number = sum_n - sum_lst
print(missing_number)

# Optimal_Approach
lst = [1, 3, 0]
xor1 = 0
xor2 = 0
for i in range(0, len(lst)):
    xor2 = xor2 ^ lst[i]
    xor1 = xor1 ^ i
xor1 = xor1 ^ len(lst)
result = xor1 ^ xor2
print(result)


# GFG
lst = [1, 0, 2, 4, 3]
n = len(lst)
for i in range(0, n+1):
    flag = 0
    for j in range(0, n):
        if lst[j] == i:
            flag = 1
            break
    if flag == 0:
        print(i)
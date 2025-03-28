nums = [1,2,2,3,1,4]
largest = 100
hash_array = [0] * (largest + 1)
for i in nums:
    hash_array[i] += 1
max_value = 0
for i in hash_array:
    if i > max_value:
        max_value = i
result = 0
for i in range(0, len(hash_array)):
    if hash_array[i] == max_value:
        result += hash_array[i]
print(result)
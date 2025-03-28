nums = [10,9,5,8]
largest = 1000000
hash = [0] * (largest + 1)
result_array = []
for i in nums:
    hash[i] += 1
for i in range(0, len(hash)):
    if i == 0 and hash[i] == 1:
        if hash[i + 1] == 0:
            result_array.append(i)
    elif i == largest and hash[i] == 1:
        if hash[i - 1] == 0:
            result_array.append(i)
    elif hash[i] == 1 and hash[i - 1] == 0 and hash[i + 1] == 0:
        result_array.append(i)
print(result_array)
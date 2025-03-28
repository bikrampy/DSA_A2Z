# Brute_Force
nums = [1,1,2,2,3,3,4]
for i in nums:
    cnt = 0
    for j in range(0, len(nums)):
        if nums[j] == i:
            cnt += 1
    if cnt == 1:
        print(i)

# Better_Approach❌
nums = [1]
maxi = nums[0]
for i in nums:
    if i > maxi:
        maxi = i
hashArray = [0] * (maxi+1)
for i in nums:
    hashArray[i] += 1
for i in range(0, len(hashArray)):
    if hashArray[i] == 1:
        print(i)

# Better_Approach✅
nums = [1,1,2,2,3,4,4]
dic = {

}
for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for key, values in dic.items():
    if values == 1:
        print(key)

# Optimal_Approach
nums = [1,1,2,3,3]
xor1 = 0
for i in nums:
    xor1 = xor1 ^ i
print(xor1)

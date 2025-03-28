# Optimal_Approach
nums = [1,2,3,4,5,6,7,8]
target = 8
index = -1
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        index = mid
        low = mid + 1
    elif target > nums[mid]:
        low = mid + 1
    else:
        high = mid - 1
print(index)
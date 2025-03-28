# Striver_Approach
nums = [1,2,3,4,8,8,9]
target = 5
ub = len(nums)
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] > target:
        ub = mid
        high = mid - 1
    elif nums[mid] <= target:
        low = mid + 1
print(ub)
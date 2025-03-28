nums = [1,2,3,4,8,8,9]
target = 5
lb = len(nums)
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
print(lb)
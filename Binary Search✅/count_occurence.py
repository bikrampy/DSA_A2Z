nums = [2,2]
target = 2
def lb(nums, target):
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
    return lb

def ub(nums, target):
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
    return ub

def count_occurence(nums, target):
    low_bound = lb(nums, target)
    upp_bound = ub(nums, target)
    if low_bound == len(nums) or nums[low_bound] != target:
        return -1
    return (((upp_bound-1)-low_bound)+1)

print(count_occurence(nums, target))
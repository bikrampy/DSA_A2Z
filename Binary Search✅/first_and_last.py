# Brute_Force
nums = [1,2,3,5,5,8,8,9]
target = 7
fst, lst = -1, -1
for i in range(0, len(nums)):
    if nums[i] == target:
        fst = i
        break
for i in range(0, len(nums)):
    if nums[i] == target:
        lst = i
print(fst, lst)

# Optimal_Approach
nums = [2,2]
target = 8
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

def first_last(nums, target):
    low_bound = lb(nums, target)
    upp_bound = ub(nums, target)
    if low_bound == len(nums) or nums[low_bound] != target:
        return [-1, -1]
    return [low_bound, upp_bound-1]

print(first_last(nums, target))

# Optimal_Approach
nums = [1,8,8,8,8,11,13]
target = 7
def first_last_occ(nums, target):
    first = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    low = 0
    high = len(nums) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return [first, last]
print(first_last_occ(nums, target))
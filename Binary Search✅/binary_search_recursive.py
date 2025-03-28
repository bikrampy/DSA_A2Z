nums = [1,2,3,4,5,6,7,8]
target = 8
low = 0
high = len(nums) - 1
def search(nums, low, high, target):
    if low > high:
        return -1
    mid = (low + high)//2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return search(nums, mid+1, high, target)
    else:
        return search(nums, low, mid-1, target)
print(search(nums, low, high, target))
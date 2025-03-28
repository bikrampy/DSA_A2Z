nums= [4,5,6,2,3]
def findMin(nums):
    low = 0
    high = len(nums) - 1
    ans = (2**64) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= nums[low]:
            ans = min(ans, nums[low])
            low = mid + 1
        elif nums[mid] <= nums[high]:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans
print(findMin(nums))
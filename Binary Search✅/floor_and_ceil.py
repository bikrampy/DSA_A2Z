# Striver_Approach
def FloorAndCeil(a, n, x):
    floor = -1
    ceil = -1
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] <= x:
            floor = a[mid]
            low = mid + 1
        else:
            high = mid - 1
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] >= x:
            ceil = a[mid]
            high = mid - 1
        else:
            low = mid + 1
    return [floor, ceil]

# My_Approach
def getFloorAndCeil(self, x: int, arr: list) -> list:
    # code here
    arr = sorted(arr)
    floor = -1
    ceil = -1
    x1 = x
    while x1 >= min(arr):
        if x1 in arr:
            floor = x1
            break
        else:
            x1 -= 1
    x2 = x
    while x2 <= max(arr):
        if x2 in arr:
            ceil = x2
            break
        else:
            x2 += 1
    return [floor, ceil]
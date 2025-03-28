def merge(lst, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if lst[left] <= lst[right]:
            temp.append(lst[left])
            left += 1
        else:
            temp.append(lst[right])
            right += 1
    while left <= mid:
        temp.append(lst[left])
        left += 1
    while right <= high:
        temp.append(lst[right])
        right += 1
    for i in range(low, high+1):
        lst[i] = temp[i-low]

def merge_sort(lst, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(lst, low, mid)
    merge_sort(lst, mid + 1, high)
    merge(lst, low, mid, high)

lst1 = [3,1,2,4,1,5,2,6,4]
lw = 0
hgh = len(lst1) - 1
merge_sort(lst1, lw, hgh)
print(lst1)
def f(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j

def quicksort(arr, low, high):
    if low < high:
        partition = f(arr, low, high)
        quicksort(arr, low, partition-1)
        quicksort(arr, partition+1, high)

lst = [4,6,2,5,7,9,1,3]
hgh = len(lst) - 1
quicksort(lst, 0, hgh)
print(lst)
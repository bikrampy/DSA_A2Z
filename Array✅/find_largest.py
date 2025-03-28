# Brute_Force
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

def qs(arr, low, high):
    if low < high:
        partition = f(arr, low, high)
        qs(arr, low, partition-1)
        qs(arr, partition+1, high)

import array as arr
a = arr.array('i', [1, 2, 4, 2, 9, 8, 2])
qs(a, 0, (len(a)-1))
largest = a[len(a)-1]
print(largest)

#Optimal_Approach
import array as arr
a = arr.array('i', [1, 2, 4, 2, 9, 8, 2])
n = len(a)
largest = a[0]
for i in range(1, n):
    if a[i] > largest:
        largest= a[i]
print(largest)
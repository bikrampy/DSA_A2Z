# Brute_Force
import array as arr
a = arr.array('i', [1, 7, 7, 7, 7, 7])
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
hgh = len(a)
qs(a, 0, (hgh-1))
largest = a[hgh-1]
second_largest = -1
for i in range(hgh-2, -1, -1):
    if a[i] < largest:
        second_largest = a[i]
        break
print(second_largest)

# Better_Approach
import array as arr
a = arr.array('i', [2, 4, 5, 7, 9, 1])
n = len(a)
largest = a[0]
for i in range(1, n):
    if a[i] > largest:
        largest= a[i]
s_largest = -1
for i in range(0, n):
    if a[i] > s_largest and a[i] < largest:
        s_largest = a[i]
print(s_largest)

# Optimal_Approach
import array as arr
a = arr.array('i', [1, 2, 4, 7, 7, 5])
n = len(a)
largest = a[0]
secLargest = -1
for i in range(1, n):
    if a[i] > largest:
        secLargest = largest
        largest = a[i]
    elif a[i] < largest and a[i] > secLargest:
        secLargest = a[i]
print(secLargest)
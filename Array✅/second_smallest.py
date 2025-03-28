# Optimal_Approach
import sys
import array as arr
a = arr.array('i', [7, 7, 9])
n = len(a)
smallest = a[0]
secSmallest = sys.maxsize
for i in range(1, n):
    if a[i] < smallest:
        secSmallest = smallest
        smallest = a[i]
    elif a[i] > smallest and a[i] < secSmallest:
        secSmallest = a[i]
print(secSmallest)

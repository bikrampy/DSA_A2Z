# Optimal_Approach
import array as arr
a = arr.array('i', [1, 7, 7])
n = len(a)
flag = True
for i in range(0, n-1):
    if a[i+1] >= a[i]:
        pass
    else:
        flag = False
        break
print(flag)
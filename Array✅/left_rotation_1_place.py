#Optimal_Approach
import array
a = array.array('i', [1, 2, 3, 4, 5])
temp = a[0]
for i in range (1, len(a)):
    a[i-1] = a[i]
a[len(a)-1] = temp
print(a)

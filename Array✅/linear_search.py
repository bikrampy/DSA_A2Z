# Optimal_Approach
lst = [1,2,3,4,5,6]
k = 7
index = -1
for i in range(0, len(lst)):
    if lst[i] == k:
        index = i
        break
print(index)
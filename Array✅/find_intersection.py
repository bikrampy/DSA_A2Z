a = [1,2,2,1]
b = [2,2]
intersection = []
n2 = len(b)
vis = [0] * n2
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j] and vis[j] == 0:
            intersection.append(a[i])
            vis[j] = 1
            break
print(intersection)

# Optimal_Approach
a = [1,1,2,2,3,3,4,5,5]
b = [2,3,3,5,6,7]
n1 = len(a)
n2 = len(b)
i = 0
j = 0
intersection = []
while i < n1 and j < n2:
    if a[i] == b[j]:
        intersection.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
print(intersection)
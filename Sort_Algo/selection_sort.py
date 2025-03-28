a = [13, 46, 24, 52, 20, 9]
for i in range(0, (len(a)-1)):
    min = i
    for j in range(i, len(a)):
        if a[j] < a[min]:
            min = j
    temp = a[min]
    a[min] = a[i]
    a[i] = temp
print(a)
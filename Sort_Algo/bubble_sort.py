a = [13, 46, 24, 52, 20, 9]
n = len(a)
for i in range(n-1, 0, -1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            tem = a[j]
            a[j] = a[j+1]
            a[j+1] = tem
print(a)
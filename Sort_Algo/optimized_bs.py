a = [1, 2, 3, 4, 5]
n = len(a)
for i in range(n-1, 0, -1):
    didSwap = False
    for j in range(0, i):
        if a[j] > a[j+1]:
            tem = a[j]
            a[j] = a[j+1]
            a[j+1] = tem
            didSwap = True
    if didSwap == False:
        break
    print("checkpoint")
print(a)
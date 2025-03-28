a = [13, 46, 24, 52, 20, 9]
for i in range(0, len(a)):
    j = i
    while j > 0 and a[j-1] > a[j]:
        tem = a[j-1]
        a[j-1] = a[j]
        a[j] = tem
        j -= 1
print(a)
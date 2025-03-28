# Using Two Pointer
def fun(l: int, r: int, a: list):
    if l >= r:
        return
    temp = a[l]
    a[l] = a[r]
    a[r] = temp
    fun(l + 1, r - 1, a)

l1 = [1, 2, 3, 5, 9, 10, 11]
fun(0, (len(l1)-1), l1)
print(l1)

# Using Single Pointer
def fun(i: int, l: list):
    n = len(l)
    if i >= (n // 2):
        return
    temp = l[i]
    l[i] = l[n - i - 1]
    l[n - i - 1] = temp
    fun(i + 1, l)

l1 = [2, 3, 1, 5, 6, 7]
fun(0, l1)
print(l1)
print(5//2)
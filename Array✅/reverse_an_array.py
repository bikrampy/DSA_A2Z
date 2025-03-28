# Without Recursion
def fun(g: list):
    a = []
    i = len(g) - 1
    while i >= 0:
        a.append(g[i])
        i -= 1
    return a

given_list = [1, 0, 9, 2, 6, 8]
print(fun(given_list))

# Without Recursion Using 2 Pointer
def fun(a: list):
    p1 = 0
    p2 = len(a)-1
    while p1 < p2:
        a[p1], a[p2] = a[p2], a[p1]
        p1 += 1
        p2 -= 1
    return a

list1 = [1, 2, 4, 3, 5, 6]
print(fun(list1))
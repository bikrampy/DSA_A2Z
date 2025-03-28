# 1st Approach
def f1(n):
    if n == 0:
        return
    print(n)
    f1(n-1)

f1(5)

# 2nd Approach (Backtracking Approach)
def f2(i, n):
    if i > n:
        return
    f2(i + 1, n)
    print(i)

f2(1, 5)
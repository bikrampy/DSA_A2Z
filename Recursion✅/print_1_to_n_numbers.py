# 1st Approach
def f1(i, n):
    if i > n:
        return
    print(i)
    f1(i + 1, n)

f1(1, 15)

# 2nd Approach (Backtracking Approach)
def f2(n: int):
    if n == 0:
        return
    f2(n - 1)
    print(n)

f2(15)

# Parameterised Approach
def f1(i, sum=0):
    if i == 0:
        print(sum)
        return
    f1(i - 1, sum + i)

f1(3)
# Functional Approach
def f2(n: int):
    if n == 1:
        return 1
    return n + f2(n - 1)

print(f2(3))
# Parameterised Approach
def f1(n: int, sm=0):
    if n < 1:
        print(sm)
        return
    f1(n - 1, sm + (n ** 3))

f1(3)
# Functional Approach
def f2(n: int):
    if n == 1:
        return 1
    return (n ** 3) + f2(n - 1)

print(f2(5))

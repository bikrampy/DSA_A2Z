# Functional Approach
def f(n: int):
    if n == 1:
        return 1
    return n * f(n - 1)

print(f(5))
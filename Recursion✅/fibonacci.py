def fun(i):
    if i <= 1:
        return i
    return fun(i - 1) + fun(i - 2)

print(fun(9))
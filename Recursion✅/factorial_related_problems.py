# Factorials_Less_than_or_Equal_to_n
def f(d: int):
    if d == 1:
        return 1
    return d * f(d - 1)

def factorialNumbers(n):
    lst = [1]
    last_factorial = 1
    x = 2
    while n > last_factorial:
        last_factorial = f(x)
        if last_factorial <= n:
            lst.append(last_factorial)
        x += 1
    return lst

# Find_whether_it_is_a_factorial_number_or_not
def f(d: int):
    if d == 1:
        return 1
    return d * f(d - 1)
def isFactorial (N):
    x = 1
    factorial = 1
    while factorial <= N:
        factorial = f(x)
        if factorial == N:
            return 1
        x += 1
    return 0
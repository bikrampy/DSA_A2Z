def check_even_odd(n : int):
    if n & 1 == 0:
        return "Even"
    else:
        return "odd"
print(check_even_odd(12))
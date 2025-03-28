def swap2numbers(a: int, b: int):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
print(swap2numbers(3, 5))
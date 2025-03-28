def checkPowerOf2(n : int):
    if n == 0:
        return "Not a power of 2."
    if n & n-1 == 0:
        return "A power of 2."
    else:
        return "Not a power of 2."
print(checkPowerOf2(128))
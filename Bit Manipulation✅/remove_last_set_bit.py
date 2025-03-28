def removeLastSetBit(n : int):
    return n & n-1
print(removeLastSetBit(7))
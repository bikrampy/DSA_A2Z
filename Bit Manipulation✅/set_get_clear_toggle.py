# Set ith Bit
def setIthBit(n: int, i: int):
    return n | (1 << i)
print(setIthBit(9, 2))
# Clear ith Bit
def clearIthBit(n: int, i: int):
    return n & (~(1 << i))
print(clearIthBit(9, 2))
# Get ith Bit
def getIthBit(n : int, i: int):
    if n & (1 << i) == 0:
        bit = 0
    else:
        bit = 1
    return bit
print(getIthBit(31, 3))
# Toggle ith Bit
def toggleIthBit(n : int, i : int):
    return n ^ (1 << i)
print(toggleIthBit(14, 2))
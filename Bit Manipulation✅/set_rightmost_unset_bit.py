def setRightmostUnsetBit(n : int):
    return n | (n + 1)
print(setRightmostUnsetBit(37))
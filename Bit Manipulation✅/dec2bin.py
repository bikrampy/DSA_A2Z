def dec2bin(x: int):
    res = ''
    while x != 0:
        if x % 2 == 1:
            res += '1'
        else:
            res += '0'
        x = x//2
    res= res[::-1]
    return res
print(dec2bin(7))

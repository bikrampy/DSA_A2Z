def bin2dec(x: str):
    num = 0
    leng = len(x) -1
    for bits in x:
        if bits == '1':
            num = num + (2 ** leng)
        leng -= 1
    return num
print(bin2dec('1'))
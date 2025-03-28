def countSetbits(num:int):
    count = 0
    while num != 0:
        if num % 2 == 1:
            count += 1
        num = num // 2
    return count

print(countSetbits(16))
import math
n = 4
lst = []
total = 0
while n > 0:
    for i in range(1, (int(math.sqrt(n)))+1):
        if n % i == 0:
            lst.append(i)
            total += i
            if n // i != i:
                lst.append(n//i)
                total += (n//i)
    n -= 1
print(total)
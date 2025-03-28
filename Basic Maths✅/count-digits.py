# Brute_Force
n = int(input())
a = 0
while n > 0:
    n = n // 10
    a += 1
print(a)

# GFG
n2 = n
count = 0
while n > 0:
    d = n % 10
    n = n // 10
    if d != 0 and n2 % d == 0:
        count += 1
print(count)
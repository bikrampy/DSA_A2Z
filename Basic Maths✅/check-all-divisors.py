# Brute_Force
ls = []
n = 21
for i in range(1, n + 1):
    if n % i == 0:
        ls.append(i)
print(ls)

# Optimal_Approach
import math
lst = []
num = 21
sqrtN = int(math.sqrt(num))
for i in range(1, sqrtN + 1):
    if num % i == 0:
        lst.append(i)
        if num // i != i:
            lst.append((num // i))
print(lst)

# GFG
n = 4
lst = []
while n > 0:
    for i in range(1, (int(math.sqrt(n))+1)):
        if n % i == 0:
            lst.append(i)
            if n // i != i:
                lst.append(n//i)
    n -= 1
print(sum(lst))
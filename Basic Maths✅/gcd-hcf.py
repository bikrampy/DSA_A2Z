# Brute_Force
n1 = 24
n2 = 27
gcd = 1
for i in range(2, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print(gcd)

# Better_Approach
x = 20
y = 15
z = min(x, y)
hcf = 1
while z > 0:
    if x % z == 0 and y % z == 0:
        hcf = z
        break
    z -= 1
print(hcf)

# Optimal Approach
def find_gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a - b
        else:
            b = b - a
    if a == 0:
        return b
    else:
        return a
print(find_gcd(23, 92))

# GFG
def lcm_gcd(a, b):
    n1 = a
    n2 = b
    gcd = 1
    while a > 0 and b > 0:
        if a >= b:
            a = a - b
        else:
            b = b - a
    if a == 0:
        gcd = b
    else:
        gcd = a
    lcm = gcd * (n1 // gcd) * (n2 // gcd)
    return [gcd, lcm]
print(lcm_gcd(23, 92))
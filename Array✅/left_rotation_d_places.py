# Brute_Force
import array
a = array.array('i', [1, 2, 3, 4, 5])
d = 7
d %= len(a)
for i in range (0, d):
    temp = a[0]
    for i in range (1, len(a)):
        a[i-1] = a[i]
    a[len(a)-1] = temp
print(a)

# Brute_Force_Striver
a = array.array('i', [1, 2, 3, 4, 5])
d = 7
d %= len(a)
temp = array.array('i', [])
for i in range(0, d):
    temp.append(a[i])
for i in range(d, len(a)):
    a[i-d]= a[i]
for i in range((len(a)-d), len(a)):
    a[i] = temp[i-(len(a)-d)]
print(a)

# Optimal_Approach
a = array.array('i', [1, 2, 3, 4, 5, 6, 7])
d = 3
n = len(a)
d %= n
# Sub_Step-1
x = 0
y = d-1
while x < y:
    tem = a[x]
    a[x] = a[y]
    a[y] = tem
    x += 1
    y -= 1
# Sub_Step-2
p = d
q = n-1
while p < q:
    tem = a[p]
    a[p] = a[q]
    a[q] = tem
    p += 1
    q -= 1
# Sub_Step-3
a.reverse()
print(a)
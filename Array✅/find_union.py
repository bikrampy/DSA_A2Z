# Brute_Force
a = [1,2,3,4,5,6]
b = [2,4,6,8]
st = set()
union = []
for i in range(0, len(a)):
    st.add(a[i])
for i in range(0, len(b)):
    st.add(b[i])
for i in st:
    union.append(i)
union.sort()
print(union)

# Optimal_Approach
a = [1,1,2,2,3,4,5,6,6]
b = [2,4,4,5,6,8]
union = []
n1 = len(a)
n2 = len(b)
i = 0
j = 0
while i < n1 and j < n2:
    if (a[i] <= b[j]):
        if a[i] not in union:
            union.append(a[i])
        i += 1
    else:
        if b[j] not in union:
            union.append(b[j])
        j += 1
while i < n1:
    if a[i] not in union:
        union.append(a[i])
    i += 1
while j < n2:
    if b[j] not in union:
        union.append(b[j])
    j += 1
print(union)
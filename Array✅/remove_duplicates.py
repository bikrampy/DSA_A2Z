# Brute_Force
import array as arr
a = arr.array('i', [1, 1, 1 , 7, 7, 7])
st = set()
for i in range(0, len(a)):
    st.add(a[i])
index = 0
for i in st:
    a[index] = i
    index += 1
print(index)

# Optimal_Approach
import array as arr
a = arr.array('i', [1, 1, 1 , 7, 7, 7])
i = 0
for j in range(1, len(a)):
    if a[i] == a[j]:
        pass
    elif a[i] != a[j]:
        a[i+1] = a[j]
        i += 1
print(a)
print(i+1)

# Brute_Force
arr = [1, 2, 3, 1, 2]
query = [1, 4, 3, 10, 2]
for item in query:
    cnt = 0
    for i in range(0, len(arr)):
        if arr[i] == item:
            cnt += 1
    print(cnt)

# 2nd_Approach
arr = [1, 2, 3, 1, 2]
query = [1, 4, 3, 10, 2]
largest = 12
hash = [0] * (largest+1)
for i in range(0, len(arr)):
    hash[arr[i]] += 1
for i in query:
    print(hash[i])
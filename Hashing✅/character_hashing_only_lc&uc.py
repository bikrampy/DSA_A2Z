# Brute_Force
input_string = "ababcdab"
query_string = "acz"
for letters in query_string:
    cnt = 0
    for i in input_string:
        if i == letters:
            cnt += 1
    print(cnt)

# Optimal_Approach(LC)
hash_array = [0] * 26
input_string = "ababcdab"
query_string = "acz"
for string in input_string:
    hash_array[(ord(string) - ord('a'))] += 1
for i in query_string:
    print(hash_array[(ord(i) - ord('a'))])

# Optimal_Approach(UC)
hash_array = [0] * 26
input_string = "BIKRAMSAHA"
query_string = "SHA"
for string in input_string:
    hash_array[(ord(string) - ord('A'))] += 1
for i in query_string:
    print(hash_array[(ord(i) - ord('A'))])
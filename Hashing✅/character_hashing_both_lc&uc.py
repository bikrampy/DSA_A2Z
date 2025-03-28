# Brute_Force
input_string = "ababcdab"
query_string = "acz"
for letters in query_string:
    cnt = 0
    for i in input_string:
        if i == letters:
            cnt += 1
    print(cnt)

# Optimal_Approach
hash_array = [0] * 256
input_string = "!BikramSahaShreyosiHalder!"
query_string = "!BSrasi"
for string in input_string:
    hash_array[ord(string)] += 1
for i in query_string:
    print(hash_array[ord(i)])

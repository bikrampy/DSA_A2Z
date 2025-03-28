# Optimal_Approach
n = 234
list_of_digits = []
while n > 0:
    list_of_digits.append(n % 10)
    n = n // 10
list_of_digits = list_of_digits[::-1]
print(list_of_digits)

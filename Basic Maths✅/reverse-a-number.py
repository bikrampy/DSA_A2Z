# Optimal_Approach
n = -7789
reversed_number = 0
sign = 1 if n > 0 else -1
n = abs(n)
while n > 0:
    last_digit = n % 10
    n = n // 10
    reversed_number = (reversed_number * 10) + last_digit
reversed_number = reversed_number * sign
print(reversed_number)

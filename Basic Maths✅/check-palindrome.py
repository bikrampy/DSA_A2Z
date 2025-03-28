# Optimal_Approach
n = 212
n2 = n
reversed_num = 0
if n < 0:
    print("Not a palindrome.")
else:
    while n > 0:
        digit = n % 10
        n = n // 10
        reversed_num = (reversed_num * 10) + digit
    if n2 == reversed_num:
        print("It is a palindrome.")
    else:
        print("Not a palindrome.")

# My_Optimal_Approach
n = 212
n2 = str(n)
revn = n2[::-1]
if revn == n2:
    print(True)
else:
    print(False)

# AngelaYu_Approach
number = 1
def check_prime_number(n: int) -> bool:
    if n > 1:
        for item in range(2, n):
            if n % item == 0:
                return False
        else:
            return True
    else:
        return False
answer = check_prime_number(number)
print(answer)

# Brute_Force
cnt = 0
n = 1
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
if cnt == 2:
    print(True)
else:
    print(False)
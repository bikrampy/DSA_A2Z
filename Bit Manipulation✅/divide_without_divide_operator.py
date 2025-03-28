# 1st Approach
def divide(dividend: int, divisor: int) -> int:
    cnt = 0
    sum = 0
    while sum + divisor <= dividend:
        cnt += 1
        sum += divisor
    return cnt
print(divide(22, 3))
# 2nd Approach
def divide(dividend: int, divisor: int) -> int:
    sign = 1
    if dividend >= 0 and divisor < 0:
        sign = -1
    if dividend < 0 and divisor > 0:
        sign = -1
    n = abs(dividend)
    d = abs(divisor)
    ans = 0
    while n >= d:
        cnt = 0
        while n >= (d << (cnt + 1)):
            cnt += 1
        ans += (1 << cnt)
        n = n - (d * (1 << cnt))
    ans = ans * sign
    if ans >= 2 ** 31:
        ans = (2 ** 31) -1
    return ans
print(divide((2 ** 31), -1))
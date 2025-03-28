# Optimal_Approach
num = 1634
arm = 0
x = num
y = num
digits = 0
while x > 0:
    x = x // 10
    digits += 1
while y > 0:
    ld = y % 10
    arm = arm + (ld ** digits)
    y = y // 10
if arm == num:
    print("True")
else:
    print("False")
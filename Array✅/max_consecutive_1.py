# Optimal_Approach
nums = [1,1,1,0,1,1,1,1,0,1]
max = 0
cnt = 0
for i in range(0, len(nums)):
    if nums[i] == 1:
        cnt += 1
    else:
        if cnt > max:
            max = cnt
        cnt = 0
if cnt > max:
    max = cnt
print(max)

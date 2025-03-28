import sys
nums = [1,2,3,1,3,3,1]
dic = {

}
for items in nums:
    if items not in dic:
        dic[items] = 1
    else:
        dic[items] += 1
# print(dic)
INT_MAX = sys.maxsize
max = 0
min = INT_MAX
for items in dic:
    # print(items)
    if dic[items] > max:
        max = dic[items]
# print(max)
for items in dic:
    if dic[items] < min:
        min = dic[items]
# print(min)
for key, value in dic.items():
    if value == max:
        print(key)
for key, value in dic.items():
    if value == min:
        print(key)
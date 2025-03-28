import sys
v = [1,2,3,1,3,3,1]
dic = {
}
for items in v:
    if items not in dic:
        dic[items] = 1
    else:
        dic[items] += 1
mx = 0
mn = sys.maxsize
for items in dic:
    if dic[items] > mx:
        mx = dic[items]
for items in dic:
    if dic[items] < mn:
        mn = dic[items]
max_element = []
min_element = []
for key, value in dic.items():
    if value == mx:
        max_element.append(key)
for key, value in dic.items():
    if value == mn:
        min_element.append(key)
elements = [min(max_element), min(min_element)]
print(elements)
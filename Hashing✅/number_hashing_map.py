arr = [1, 2, 1, 3, 2]
query = [1, 3, 4, 2, 10]
dic = {

}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for item in query:
    print(dic.get(item, 0))
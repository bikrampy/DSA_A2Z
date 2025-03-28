str = "aabcdcac"
query = "abz"
dic = {

}
for i in str:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for item in query:
    print(dic.get(item, 0))
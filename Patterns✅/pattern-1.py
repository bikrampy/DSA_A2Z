i = 0
while i < 4:
    j = 0
    while j < 4:
        print('*', end="")
        j += 1
    i += 1
    print("")
print("=============")
var = int(input())
for i in range(var):
    for j in range(var):
        print("*", end="")
    print("")

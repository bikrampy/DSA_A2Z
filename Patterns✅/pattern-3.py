def pattern3(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, "", end="")
        print("")


pattern3(19)

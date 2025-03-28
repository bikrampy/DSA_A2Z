def pattern10(n: int):
    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end="")
        print("")
    for i in range(1, n):
        for j in range(1, n - i + 1):
            print("* ", end="")
        print("")


pattern10(4)

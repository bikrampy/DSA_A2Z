def pattern7(n: int):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", " ", end="")
        for j in range(1, 2 * i):
            print("*", " ", end="")
        for j in range(1, n - i):
            print(" ", " ", end="")
        print("")


pattern7(5)

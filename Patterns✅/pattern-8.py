def pattern8(n: int):
    for i in range(1, n + 1):
        for j in range(1, i):
            print(" ", " ", end="")
        for j in range(1, 2 * n - 2 * i + 2):
            print("*", " ", end="")
        for j in range(1, i):
            print(" ", " ", end="")
        print("")


pattern8(6)

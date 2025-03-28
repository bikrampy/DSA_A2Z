def fib(n):
    if n <= 1:
        print(n)
    else:
        fib_l = [0, 1]
        for i in range(2, n+1):
            fib_l.append(fib_l[i-1] + fib_l[i-2])
        print(fib_l[n])

fib(4)
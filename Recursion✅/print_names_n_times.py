def f(n: int,s: str):
    if n == 0:
        return
    print(s)
    f(n-1, s)

f(5, "Bikram")
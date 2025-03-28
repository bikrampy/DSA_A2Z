# Approach 1
def fun(l, r, s:str):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return fun(l+1, r-1, s)

print(fun(0, 4, "Madam".lower()))

# Approach 2
def fun(i: int, s: str):
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return fun(i + 1, s)

print(fun(0, "string1"))
def binary(x):
    if x == 0:
        return "0"
    res = []
    while x > 0:
        res.append(str(x%2))
        x //= 2
    return "".join(res[::-1])

n = int(input())
print(binary(n).zfill(10))
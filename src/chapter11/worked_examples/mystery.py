def mystery(n):
    if n <= 0:
        return 0
    else:
        smaller = n - 1
    return mystery(smaller) + n * n


print(mystery(4))  # 1^2 + 2^2 + 3^2 + 4^2

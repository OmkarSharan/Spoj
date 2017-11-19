def primeGenarator(m, n):
    if m <= 2:
        yield 2
    if m == 1:
        m = 3
    elif m % 2 == 0:
        m = m + 1
    siev = set(range(m, n + 1, 2))
    upper = int(n ** 0.5) + 1
    for i in range(3, upper, 2):

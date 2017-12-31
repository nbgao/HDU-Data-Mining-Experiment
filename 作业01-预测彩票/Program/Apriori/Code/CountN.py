def CountN(F, n):
    sum  = 0
    L = []
    for f in F:
        if len(f) == n:
            sum += 1
            L.append(f)

    return sum, L

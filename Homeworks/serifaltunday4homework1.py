def serif(start, end):
    out = list()
    if start <= 1:
        start = 2

    altun = [True] * (end + 1)
    for p in range(start, end + 1):
        if (altun[p]):
            out.append(p)
            for i in range(p, end + 1, p):
                altun[i] = False
    return out
print(serif(1, 100))

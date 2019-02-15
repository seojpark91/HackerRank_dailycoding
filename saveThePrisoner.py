def saveThePrisoner(n, m, s):
    if s + m < n:
        return s+m-1
    else:
        if (s + m -1) % n ==0:
            return n
        else:
            return (s+m -1) % n
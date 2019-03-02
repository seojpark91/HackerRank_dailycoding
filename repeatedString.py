def repeatedString(s, n):
    q = n // len(s)
    rem = n % len(s)
    index = rem-1
    a = []
    for i, j in enumerate(s):
        if j == 'a':
            a.append(i)
    if rem:
        return q * len(a) + len(list(filter(lambda x: x<=index, a)))
    else:
        return q * len(a)
    
repeatedString('aba', 10), repeatedString('a', 1000000000000)
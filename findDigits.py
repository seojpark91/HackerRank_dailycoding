def findDigits(n):
    res = 0
    digits = [s for s in str(n)]
    
    for d in digits:
        try:
            n%int(d)
        except ZeroDivisionError:
            res += 0
        else:
            if n%int(d) == 0:
                res += 1
    return res
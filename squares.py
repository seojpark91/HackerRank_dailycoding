def squares(a, b):
    n1 = math.ceil(math.sqrt(a))
    n2 = math.floor(math.sqrt(b))
    res = n2-n1
    if res == 0:
        if n1 == n2:
            return 1
        else:
            return res
    else:
        return res+1
    
squares(4, 4), squares(16, 49), squares(11, 754)
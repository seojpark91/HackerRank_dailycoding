def kaprekarNumbers(p, q):
    res = []

    for n in range(p, q+1):
        if n < 4:
            sq = n**2
            num = '0' + str(sq) 
            r,l = num[-1], num[:-1]
            r, l = int(r), int(l)
            if r+l == n:
                res.append(n)
            
        else:
            sq = n**2
            num = str(sq)
            d = len(str(n))
            r, l = num[-d:], num[:-d]
            r, l = int(r), int(l)
            if r+l == n:
                res.append(n)
    
    if res:
        print(*res)
    else:
        print("INVALID RANGE")

kaprekarNumbers(1,100), kaprekarNumbers(100,300)
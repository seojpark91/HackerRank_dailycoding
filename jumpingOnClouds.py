def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = k%n
    e -= c[i] *2 +1
    
    while i !=0:
        i = (i+k)%n
        e -= c[i] *2 +1
        
    return e
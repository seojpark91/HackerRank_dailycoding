def stones(n, a, b):
    """
    n : the number of stones
    a : one possible integer difference
    b : another possible integer difference
    
    In this problem, it is important to realize permutation of possible differences containing the same amount of a and b 
    will have the same result. Therefore, number of stones n gives n distinct results. For example, if there are 4 stones, 
    there are 4 possible results : 0 + a + a + a, 0 + a + a + b, 0 + a + b + b, 0 + b + b + b. 
    """
    ls = []
    for i in range(0,n):
        ls.append(i*a + (n-1-i)*b)
    return sorted(list(set((ls))))

stones(4,10,100), stones(3,1,2)
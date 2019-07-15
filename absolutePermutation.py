def absolutePermutation(n, k):
    """
    return an integer that represents the smallest lexicographically smallest permutation, or -1 if there is none
    parameters:
    n: the upper bound of natural numbers to consider, inclusive
    k: the integer difference between each element and its index
    """
    if k == 0:
        return list(range(1, n+1))
    
    elif (n/k) % 2 != 0:
        return [-1]
    
    else:
        add = True
        res = []
        
        for i in range(1, n+1):
            if add:
                res.append(i+k)
            else:
                res.append(i-k)
                
            if i % k == 0:
                if add:
                    add = False
                else:
                    add = True
        return ' '.join([str(i) for i in res])

if __name__ == '__main__':
    print(absolutePermutation(100,2))
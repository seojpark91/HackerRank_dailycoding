def biggerIsGreater(w):
    # finding non-increasing suffix
    idx = len(w) - 1
    while idx>0 and w[idx-1] >= w[idx]:
        idx -= 1
    if idx <=0:
        return 'no answer'
    #finding succesor to pivot
    j = len(w) - 1
    while w[j] <= w[i-1]:
        j -= 1
    w[i-1], w[j] = w[j], w[i-1]
    
    #reverse
    w[i:] = w[len(w)-1: i-1 : -1]
    return w
    
biggerIsGreater('ab'), biggerIsGreater('bb'), biggerIsGreater('hefg'), biggerIsGreater('dhck'), biggerIsGreater('dkhc')
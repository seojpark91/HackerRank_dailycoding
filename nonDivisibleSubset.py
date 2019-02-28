def nonDivisibleSubset(k, S):
    residuals = [i%k for i in S]
    counter = [0] * k
    
    for r in residuals:
        counter[r] +=1
    c = min(counter[0], 1)

    for i in range(1, (k//2)+1):
        if i != k-i:
            c += max(counter[i], counter[k-i])
        elif i == k-i:
            c += min(counter[i], 1)
    return c

S1 = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k1 = 7

S2 = [1, 7, 2, 4]
k2 = 3
nonDivisibleSubset(k1, S1), nonDivisibleSubset(k2, S2)
def beautifulPairs(A, B):
    """
    return an integer that represents the maximum number of pairwise disjoint beautiful pairs that can be formed
    
    A: an array of integers
    B: an array of integers
    """
    n = len(A)
    # count values in each array A and B
    counter_A = Counter(A)
    counter_B = Counter(B)
    # get number of common pairs 
    n_common_pairs = sum(min([counter_A[i], counter_B[i]]) for i in counter_A.keys())
    # when A and B have the same number of elements, since the condition states that one of the values in B must be changed, the number of common pairs is one less  
    return n_common_pairs-1 if n_common_pairs==n else n_common_pairs+1
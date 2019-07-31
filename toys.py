def toys(w):
    """
    return the minimum number of containers required to ship
    
    parameter:
    w: an array of integers that represent the weights of each order to ship
    """
    n_container = 0
    w = set(w)
    while len(w) > 0:
        min_weight = min(w)
        n_container += 1
        w = w.difference(set(range(min_weight, min_weight + 4 + 1)))
        
    return n_container